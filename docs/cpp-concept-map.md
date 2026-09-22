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
