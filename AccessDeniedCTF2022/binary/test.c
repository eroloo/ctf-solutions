int main()
{
	for (int i=0; i<100; i++)
	{
		int a = rand();
		printf("%d,", a >> 0x1f >> 2);
	}
}
