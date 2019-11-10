#include <stdio.h>

void no_function() {
    /*
    関数を使わない場合
    */
    int n = 1;
    printf("----------\n");
    printf("debug: %d\n", n);
    printf("----------\n");
    n++;
    printf("----------\n");
    printf("debug: %d\n", n);
    printf("----------\n");
    n++;
    printf("----------\n");
    printf("debug: %d\n", n);
    printf("----------\n");
}

void debug(int n) {
    /*
    今回使う関数
    */
    printf("----------\n");
    printf("debug: %d\n", n);
    printf("----------\n");
}

void with_function() {
    /*
    関数を使う場合
    */
    int n = 1;
    debug(n);
    n++;
    debug(n);
    n++;
    debug(n);
}

int main() {
    no_function();
    with_function();
    return 0;
    /*
    出力
    ----------
    debug: 1
    ----------
    ----------
    debug: 2
    ----------
    ----------
    debug: 3
    ----------
    */
}