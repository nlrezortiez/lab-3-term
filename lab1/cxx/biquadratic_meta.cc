#include <iostream>
#include <limits>
#include <tuple>
#include <utility>
#include <numbers>

#ifndef A
 #define A (0)
#endif

#ifndef B
 #define B (0)
#endif

#ifndef C
 #define C (0)
#endif

namespace detail {
double constexpr sqrtNewtonRaphson(double x, double curr, double prev) {
    return curr == prev ? curr
                        : sqrtNewtonRaphson(x, 0.5 * (curr + x / curr), curr);
}
}  // namespace detail

double constexpr ce_sqrt(double x) {
    return x >= 0 && x < std::numeric_limits<double>::infinity()
               ? detail::sqrtNewtonRaphson(x, x, 0)
               : std::numeric_limits<double>::quiet_NaN();
}

template <typename TupleType, std::size_t... Idxs>
void print(const TupleType& tuple, std::index_sequence<Idxs...> /*unused*/) {
    std::cout << "(";
    (..., (std::cout << (Idxs == 0 ? "" : ", ") << std::get<Idxs>(tuple)));
    std::cout << ")\n";
}

template <typename... T>
void print(const std::tuple<T...>& tuple) {
    print(tuple, std::make_index_sequence<sizeof...(T)>());
}

template <int N>
static constexpr bool is_positive = N > 0;

template <int a, int b, int c>
struct solve {
        static constexpr std::tuple<double, double, double, double> answer = 
        {ce_sqrt((-b + ce_sqrt(b * b - 4 * a * c)) / (2 * a)),
         ce_sqrt((-b - ce_sqrt(b * b - 4 * a * c)) / (2 * a)),
         -ce_sqrt((-b + ce_sqrt(b * b - 4 * a * c)) / (2 * a)),
         -ce_sqrt((-b - ce_sqrt(b * b - 4 * a * c)) / (2 * a))};
};

template <int b, int c>
struct solve<0, b, c> {
    static constexpr std::tuple<double, double> answer = 
        is_positive<c> ? std::tuple<double, double>{std::numeric_limits<double>::quiet_NaN(), 
                                                    std::numeric_limits<double>::quiet_NaN()} 
                       : std::tuple<double, double>{ce_sqrt(static_cast<double>(-c)/b), 
                                                    -ce_sqrt(static_cast<double>(-c)/b)};
};

template <int c>
struct solve<0, 0, c> {
    static constexpr std::tuple<double> answer = {std::numeric_limits<double>::quiet_NaN()};
};

template <>
struct solve<0, 0, 0> {
    static constexpr std::tuple<double> answer = {std::numeric_limits<double>::infinity()};
};

int main(int argc, char** argv) {
    print(solve<A, B, C>::answer);
    return EXIT_SUCCESS;
}
