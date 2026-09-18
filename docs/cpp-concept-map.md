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
    - ❓待补实验
  - 有名字的右值是左值
    - ❓待补实验
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
- 移动构造/移动赋值  抑制 拷贝构造+拷贝赋值 = delete
### 抑制的后果
- std::move 三种静默退化成拷贝构造的情况
  - const T a; T b = std::move(a);
    - 原因：std::move(a)对const T取出来的是const  T&&,绑定不到T&&形参上，所以只能退成const T&
      - ❓待补实验
  - 只实现了析构/拷贝构造/拷贝赋值中的任意一个/全部
    - 这三个成员函数会抑制移动构造和移动赋值
      - day2_gen_rules.cpp（Test1 vs Test2 对照）
  - 移动构造没标noexcept
    - 因为vector扩容时，如果移动构造函数加了noexcept，就会采用移动构造，如果没有加，就会走拷贝构造，造成性能损失
      - ❓待补实验
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
          - ❓待补实验（day2_gen_rules.cpp 里没有 vector，测不出扩容退化）
- =delete
  - 普通函数使用时，功能是禁止这个重载被选中
    - day4_noncopyable.cpp
  - 构造函数使用时，是禁止生成默认构造函数
    - day4_noncopyable.cpp
- =default
  - 使用编译器默认生成
    - day2_gen_rules.cpp
      - ❓待补实验
