#ifndef int fat(int n){if(n==1)return 1;return n*fat(n-1);}#endif int main(int argc,char *argv[]){int x=fat(10);return 0;}