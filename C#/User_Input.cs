//this is a simple input and out generator
using System;
class Program
{
    static void Main
    {
        // user gives input
        Console.Write("Enter Your Name:");
        string Name = Console.Readline();
    //output greetings
    Console.WriteLines("Hello"+Name+"!");
        //closing window
        Console.WriteLine("Press any key to exit....");
        Console.ReadKey();
    }
}