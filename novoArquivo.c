#ifndef

int fat(int n)
{
	if (n == 1)
		return 1;
	return n*fat(n-1);
}

#endif


int main()
{
	int x = fat(2);
	return 0;
}