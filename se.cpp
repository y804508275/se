#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <Windows.h>

void square(int m, int n)
{
	float x, y, sum, z, t, r;
	if (m == 1)
	{
		sum = 1;
	}
	if (m == 2 || m == 3 || m == 4 || m == 5)
	{
		for (y = (sqrt(2) / 2); y < 1; y = y + 0.00000001)
		{
			x = y;
			z = sqrt(x * x + y * y);
			t = sqrt(z * z - y * y);
			r = sqrt(pow((y - (sqrt(2)) / 2), 2) + pow((x - (sqrt(2)) / 2), 2));
			if (t + r >= 1)
			{
				break;
			}
		}
		sum = (m - 1) * pow(r, 2) + pow(n, 2);
	}
	printf("%f", sum);
}

void main()
{
	int xx, yy, rr, m;
	double sum;
	rr = 1;
	xx = 0;
	yy = 0;
	printf("请输入有多少个圆（小于等于5）：");
	scanf_s("%d", &m);
	square(m, r0);
	Sleep(1000000000);
}
