using System;

namespace Hourglass
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = 4;
            HourlyGlass(num);
        }

        static void HourlyGlass(int num)
        {
            int i, j, k;

            for (i = 1; i <= num; i++)
            {
                for (k = 1; k < i; k++)
                    Console.Write(" ");

                for (j = 1; j <= num-i+1; j++)
                    Console.Write(j + " ");

                Console.WriteLine();
            }

            for (i = 1; i <= num - 1; i++)
            {
                for (k = 1; k < num - i; k++)
                    Console.Write(" ");

                for (j = 1; j <= i+1; j++)
                    Console.Write(j + " ");

                Console.WriteLine();
            }
        }
    }
}
