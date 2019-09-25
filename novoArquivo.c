#ifndef

int fat(int n)
{
	if (n == 1)
		return 1;
	return n*fat(n-1);
}

#endif



/* Funcao main() 
* @param argc
* @param argv
*/
int main(int argc, char *argv[])
{
	// Funcao fat
	int x = fat(10);
	return 0;
}
