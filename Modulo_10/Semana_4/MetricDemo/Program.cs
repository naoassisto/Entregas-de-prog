using System;
using System.Diagnostics.Metrics;
using System.Threading;

class Program
{
    private static readonly Meter s_meter = new Meter("HatCo.Store");
    private static readonly Counter<int> s_hatsSold = s_meter.CreateCounter<int>("hatco.store.hats_sold");

    static void Main(string[] args)
    {
        Console.WriteLine("Press any key to exit");
        while (!Console.KeyAvailable)
        {
            Thread.Sleep(5);  // Simulate a sale every second
            s_hatsSold.Add(4);  // Each sale sells 4 hats
        }
    }
}
