# C++
## 资源管理
### RAII基本概念
- RAII 是把资源的生命周期和对象的生命周期绑定，在构造函数中申请资源，在析构函数中释放资源。
  - week-01\day2_file_handle.cpp
- 为什么析构函数在错误路径下也能执行：因为C++的栈展开机制，确保了在抛出异常时，所有已经被构建的对象的析构函数都能被调用，确认资源正确释放。
### 为什么需要移动/拷贝
- 当类持有一个资源的时候，拷贝/赋值的时候，我们需要正确的处理内部资源，如果处理不正确，可能会造成double free的问题
  - day1_string.cpp
- 左值
  - 左值全部可以取地址
    - 正面：std::cout << &a 打出 000000E217CFFB50
    - 反面（#ifdef 编译期对照，一次只放一行）：
      - &10 → C2101「常量上的"&"」（字面量是纯右值，没有对象也没有存储位置）
      - &(a+1) → C2102「"&"要求左值」
      - &std::move(a) → C2102（注意：a 本身有地址，但 std::move(a) 这个**表达式**的结果是右值）
    - 字面量报 C2101、表达式报 C2102 —— 编译器本身也把这两者当不同原因
      - day7_value_category.cpp test3
  - 有名字的右值是左值
    - probe(int&)/probe(int&&) 重载探针实测：test2(int&& x) 里 probe(x) 打印「左值」
      - day7_value_category.cpp
    - 后果：void f(Widget&& w){ Widget b = w; } 走的是拷贝，要移动必须再写一次 std::move(w)
### C++类的特殊成员函数
- 默认构造函数
  - T(){} `tag:[C++98]`
- 析构函数
  - ~T(){} `tag:[C++98]`
- 拷贝构造函数
  - T(const T&){} `tag:[C++98]`
- 拷贝赋值函数
  - T& operator=(const T&){return *this;} `tag:[C++98]`
- 移动构造函数
  - T(T&&){} `tag:[C++11]`
- 移动赋值函数
  - T& operator=(T&&){return *this;} `tag:[C++11]`
- day1_string.cpp
### Rule 0/3/5
- Rule of 0
  - 类不持有裸资源，而是交给string/vector/unique_ptr去管理的时候，不需要手动实现特殊成员函数。
    - day3_rule_of_zero.cpp
- Rule of 3 `tag:[C++98]`
  - 实现析构函数/拷贝构造/拷贝赋值函数中任意一个时，会抑制移动构造和移动赋值，导致std::move退化走拷贝构造
    - day2_gen_rules.cpp
- Rule of 5 `tag:[C++11]`
  - 如果你需要实现五个特殊成员函数中的任意一个，通常需要五个都实现。实现移动构造/移动赋值时，会导致拷贝构造和拷贝复制=delete
    - day2_gen_rules.cpp
### 抑制规则表
- 析构/拷贝构造/拷贝赋值  抑制 移动构造+移动赋值 退化成拷贝
  - day7_debt_clear.cpp 实验1
- 移动构造/移动赋值  抑制 拷贝构造+拷贝赋值 = delete
  - day7_debt_clear.cpp test3（#ifdef 编译期对照：关=exit 0 / 开=exit 2）
  - 编译器原话：「由于"D3"具有用户定义的 移动构造函数，因此已隐式删除函数」（C2280 的 note 行）
- 拷贝构造 =delete **不会**连坐拷贝赋值
  - day7_debt_clear.cpp 实验2（D4 只 delete 拷贝构造，b=a 仍编过，
    用 D10 成员打印逼出真实调用链证明走的是拷贝赋值）
### 抑制的后果
- std::move 三种静默退化成拷贝构造的情况
  - const T a; T b = std::move(a);
    - 原因：std::move(a)对const T取出来的是const  T&&,绑定不到T&&形参上，所以只能退成const T&
      - day7_debt_clear.cpp（D5 有移动构造但 const 挡住 → 走拷贝构造）
  - 只实现了析构/拷贝构造/拷贝赋值中的任意一个/全部
    - 这三个成员函数会抑制移动构造和移动赋值
      - day2_gen_rules.cpp（Test1 vs Test2 对照）
  - 移动构造没标noexcept
    - 因为vector扩容时，如果移动构造函数加了noexcept，就会采用移动构造，如果没有加，就会走拷贝构造，造成性能损失
      - day7_debt_clear.cpp（D7 无 noexcept → 两次 copy constructor / D8 有 noexcept → 两次 move constructor）
      - 机制：扩容要保证强异常安全，搬到一半抛异常无法回退，所以移动不保证不抛时宁可拷贝
### vector 均摊与容量（W3，09-22 闭卷独立答对）
- 扩容三件事：申请新内存 → 拷贝/移动旧元素 → 释放旧内存
  - week-03/my_vector.h push_back
- 翻倍扩容：push n 个总搬运量 S = 4+8+...+2^(k-1) = 2^k-4 = cap_-4
  - 为什么 cap_ < 2n：最后一次扩容触发条件是 cap_/2 + 1 <= n → cap_ <= 2n-2 < 2n
  - ⚠️ 前提：**至少扩容过一次**。教练实跑 n=1..100 探针：n=1、n=2 时 cap 恒为初始 4，不成立
  - 界是紧的：n=5 时 cap=8，2n-2=8，取等
- 迭代器失效：扩容 → 旧内存释放 → 全部失效；未扩容 → 只有 end 失效
  - ✅ **09-23 闭卷独立答对**（本人自己从昨天 placement new 搬运循环推出来的）
  - 实测（`iter_probe.cpp`）：`cap 4→6` 时 `v[2]` 地址 `...A898→...A9D8` 变；
    `reserve(10)` 不扩容版地址不变。⚠️ **MSVC 增长是 1.5 倍不是 2 倍**
### 容器选型：map vs unordered_map（W3，09-23 教练讲 + 实测）
- 五条「故意选更慢的 map」的理由：
  1. **有序** —— 拆成两件事：①遍历即升序 ②`lower_bound`/`upper_bound` **动态范围查询**
     - `lower_bound(X)` = 第一个 key **≥ X** 的迭代器；`upper_bound(X)` = 第一个 key **> X**；找不到返回 `end()`
     - `[lower_bound(A), upper_bound(B))` = 所有 key 落在 [A,B] 的元素
     - **unordered_map 没有这两个函数**：哈希把 key 打散进桶，桶内顺序与 key 大小无关
     - ⚠️ 只有①能靠「存完再排一次序」补上；②补不上（排序是一次性快照，插一个就作废）
  2. **迭代器稳定**（见下「迭代器失效·关联容器」）
  3. **最坏复杂度有保证** —— 红黑树最坏 O(log n)；哈希碰撞可退化 O(n)。
     key 来自外部输入且攻击者可控时 = **HashDoS**。浏览器里 URL/域名/header/cookie/DOM id 全是外部输入
     - ⚠️ HashDoS 攻击形态本身确定；**Chromium 哪个模块因此选有序容器，教练未实查，不得当结论**
  4. **key 的成本** —— 见下「key 要求」。自定义类型进 map 只欠一个 `operator<`
  5. **不需预估规模** —— unordered_map 要 `reserve` 才能避免反复 rehash
- **key 要求**（`key_probe.cpp` MSVC 实测）：
  - `std::map<K,V>`：K 要能比大小（默认 `std::less<K>` → 要 `operator<`）
  - `std::unordered_map<K,V>`：要**两样** —— `std::hash<K>` 有特化 **且** K 支持 `operator==`
    （先算 hash 定桶，桶内再逐个 `==` 比对）
  - 标准库已特化 `std::hash` 的：内置整数/浮点/指针、`std::string` 系列、**以及枚举类型**（C++14 起标准要求）
  - ✅ 实测 `unordered_map<enum class, int>` **C++17 / C++14 均编译通过**，hash=12478008331234465636
    - 📌 **教练 09-23 出错**：断言「enum class 那题其中一个编译不过」，**没跑就说，实测两边都过**，已收回
  - ❌ 实测 `unordered_map<自定义struct>` 编译失败：`xhash(118) error C2064`（无 `std::hash` 特化）
  - **q-framework 实证**：`ui/dui/Control/UIMenu.cpp:1417` 的 `std::map<CDuiString, bool>` ——
    CDuiString 是 DuiLib 自有类，`std::hash` 不认识它 → **选 map 是成本考量，不是性能考量**
### 迭代器失效 · 关联容器（W3，09-23）
- **`map`/`set`（节点式，红黑树）**：元素各自在堆上独立分配，插入不搬动别人
  - `insert` → **不失效任何迭代器**；`erase` → **只失效被删的那一个**
  - ❌ 本人 09-23 答「全部失效」，错。实测：`find(2)` 地址 `...80C40`，
    插 100 个元素 + `erase(4)` 后地址不变、值仍 20、`++it` 正常跳到下一个存活元素
- **`unordered_map` rehash**：**使迭代器失效，但不使指向元素的指针和引用失效**
  - ⚠️ 本人 09-23 结论对（「全失效」）但理由缺，且这层区别正好被跳过
  - 实测：`bucket_count 8 → 512`（真 rehash 了），但 key=2 的**元素地址前后不变**，
    用旧地址仍读出 20 → **搬的是桶数组里的指针，不是节点本身**
  - 📌 待本人核 cppreference unordered_map 页原文后销账
- **`vector::insert`**：与 `push_back` 同理 —— **扩容则全失效**；不扩容才只失效「插入点及其后」
  - ⚠️ 本人 09-23 只答了后半句。形态定名：**同一份规则在相邻两题里只用了一半**
- ❓ 待答（09-23 布置，**09-24 两轮又绕开，第二次**，顺延 09-28）：`map` 慢，什么场景**故意**选它？
  ——「有序」不够，要落到 q-framework 里具体哪种数据 / 哪种 key 进不了 `unordered_map`
  **允许答「翻了没找到」，不允许继续不答**
- ✅ **09-24 答对（本人原话）**：rehash 之后迭代器与元素地址**不是同一回事** ——
  「**节点没搬，搬的是桶里指针、没搬的是节点**」。这解释了两件事为何同时成立不矛盾。
  ⚠️ **但本人自己指出该探针是教练跑的，对他是二手证据** → **09-28 自己重跑 `key_probe.cpp` 才算结账**
- ✅ **09-24 答对**：vector 扩容失效标准写「可能」不写「一定」—— 不扩容时只有 `end()` 失效；
  且追问的 `vector::insert` 也答对（「插入点之后全失效，触发扩容则全部失效」），
  与 cppreference 原文 `Otherwise, only the iterators and references before the insertion point remain valid.` 一致
- ✅ **09-24 第二轮答对**：`lower_bound(k)` = 第一个 **≥k** 的迭代器，`upper_bound(k)` = 第一个 **>k**；
  **end 的触发条件是「没有 ≥k / >k 的 key」，不是「k 不存在」**。
  ❌ 第一轮答「k 不存在时返回 end」被教练实跑驳回（MSVC `map{1,3,5}`）：
  `lower_bound(2)` → `key=3`（2 不存在但不是 end）；`lower_bound(7)` → `end`
- ❓ **待答（09-24 遗留，顺延 09-28）**：「遍历有序」vs「动态范围查询」的判据还差一层 ——
  本人答「插入就把排序打乱了」**不严谨**（插到 `lower_bound` 算出的正确位置上 `vector` 照样有序）。
  真代价是「后面的元素要**搬**」，这是 O(?)，`map` 是 O(?)
- ❓ **待答（09-24 遗留，顺延 09-28）**：`map` 要的是 `operator<` 不是 `operator>`
  （本人 09-24 答错）；`unordered_map` 要 hash + **`operator==`**（本人漏了后者）——
  **有了 hash 为什么还非要 `operator==`**？（两个不同 key 撞进同一个桶怎么办）
- ❓ **待答（09-24 答「记不得了」，教练只给出处未给答案）**：`unordered_map::insert` 之后
  迭代器是否失效？出处：cppreference `unordered_map::insert` 页「If after the operation...」段
  （关键词 `rehashing` / `invalidated`）
- ❓ 待答：`std::map<std::string, std::vector<Observer*>>` 遍历中调 `o->OnPrefChanged(key)`
  是虚函数 —— 若某个 Observer 在里面调了 `RemoveObserver` 会发生什么？
  （「迭代器稳定」真正咬人的形态，q-framework `pref_service.h:125` 实例）
- ⚠️ **MSVC 陷阱（09-23 教练实跑）**：`__cplusplus` 默认返回假值 `199711L`，
  必须加 `/Zc:__cplusplus` 才是真值（实测 `201402`）。据假值推出的结论一律作废重推
### copy-and-swap（09-22 结账）
- 一个 `operator=(MyVector other)` 同时当拷贝赋值和移动赋值
  - 形参 other 在**调用点**被构造：源是左值 → 拷贝构造填它；源是右值 → 移动构造填它。函数体不知情
  - week-03/my_vector.cpp test4 实测：`b=a` → MyVector copy constructor；`b=std::move(a)` → MyVector move constructor
  - ⚠️ 分辨力提醒：`MyVector<T> e = a;` 是**初始化走构造**，不是赋值，拿它测 operator= 无效
- 强异常保证 = 可能抛的动作全部发生在碰 `*this` 之前（**不是**「出错能回滚」）
  - 手写拷贝赋值：先 delete 再 new，new 抛 bad_alloc 时旧资源已毁 → 只有基本保证
  - copy-and-swap：拷贝/移动构造发生在进函数体之前，失败时 `*this` 三个成员一个没动
  - week-03 实测：异常后 size=4 cap=4 未变，析构 8 次无泄漏，退出码 0
- swap 为什么能 noexcept：交换的是 T* 与 size_t，基本类型赋值不抛
  - noexcept 函数真抛 → std::terminate，栈展开**前**终止，外层 try/catch 接不住
- 自赋值：自己和自己交换无害，不需要 `if (this != &other)`
### 申请内存 ≠ 构造对象（09-22 结账，本人自行搜索 + 改造 + 自建对照实验）
- `new T[4]` 会调 T 的默认构造 → 要求 T 默认可构造，std::vector 不要求
- 拆开两件事：`::operator new(n*sizeof(T))` **只要内存不构造**
  → `::new (addr) T(...)` **placement new，只在已有内存上构造不申请**
  → 析构时显式 `addr->~T()` 逐个析构，再 `::operator delete` 还内存
  - week-03/my_vector.h：构造/拷贝构造/扩容/push_back 四处
- 为什么非改不可：在没构造过的内存上调 `operator=` 是未定义行为
  （赋值运算符是成员函数，它会去读「自己原来的状态」）
  - `NO_PLACEMENT_NEW` 编译期对照（本人自建）：D11 加 `std::string str` 成员并在 operator= 打印
    - 开：`constructor→copy constructor→destructor`，无 copy assignment，退出码 0
    - 关：乱码 → **段错误 退出码 139**（读到未初始化内存当指针去 free）
  - ⚠️ 分辨力：纯打印的探针（成员不碰）照不出这个 bug，必须有**真实持有资源的成员**
- 扩容的异常安全回滚（本人独立改对）：`count` 提到 try 外 → catch 只析构 `[0,count)` 已构造的
  → `::operator delete(temp)` → `throw;` 原样重抛；销毁旧元素与改 `data_/cap_` 全部挪到 try 之后
  - Boom 探针实跑（第 3 次拷贝构造抛）：size/cap 4→4 未变、存活对象 4→4 无泄漏、
    异常后继续 push 成功 → 强异常保证成立
- ❓ 待想：手动 try/catch 回滚 vs RAII 守卫（unique_ptr，零 catch），标准库为什么选后者
## 工具箱
### 关键字
- explicit
  - 防止隐式转换。
    - 怎么区分语境转换和隐式转换？
      - 语境转换
        - if/while/for 的条件
        - && || ！的操作数
        - 三元表达式
        - static_assert/noexcept 操作数
      - 隐式转换
        - bool x = p
    - 使用场景
      - explicit operator bool()
        - operator bool()是类型转换运算符
          - day4_uniqueptr_test.cpp
        - operator ()()是调用运算符
- noexcept
  - 向编译器承诺函数不抛出异常
    - 使用场景
      - 移动构造必须添加noexcept
        - 因为vector扩容时，如果移动构造函数加了noexcept，就会采用移动构造，如果没有加，就会走拷贝构造，造成性能损失
          - day7_debt_clear.cpp（D7/D8 对照，实跑证据）
- =delete
  - 普通函数使用时，功能是禁止这个重载被选中
    - day4_noncopyable.cpp
  - 构造函数使用时，是禁止生成默认构造函数
    - day4_noncopyable.cpp
- =default
  - **算「用户声明」** —— 这是它和「什么都不写」的真正区别，不是「使用编译器默认生成」
    - 写了 ~T() = default 照样抑制移动生成，std::move 静默退化成拷贝
      - day7_debt_clear.cpp 实验1（D1 有 ~D1()=default → D10 copy constructor；D2 什么都不写 → D11 move constructor）
    - ⚠️ static_assert(is_move_constructible_v<T>) 对这题**无分辨力**：两侧都为真
      （const& 能绑右值，traits 问的是能否构造，不是走哪条路）。必须用带打印的实例化才能分开
