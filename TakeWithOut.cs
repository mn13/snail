using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace TakeWithOut
{
    class Program
    {
        static IEnumerable<int> TakeWithOut(IEnumerable<int> sequence, int n)
        {
            IEnumerator<int> enumerator = sequence.GetEnumerator();
            Queue<int> buf = new Queue<int>(n+1);
            int i = 0;
            while (enumerator.MoveNext())
            {
                buf.Enqueue(enumerator.Current);
                ++i;
                if (i >= n)
                    yield return buf.Dequeue();
            }
            if (i < n)
                yield break;
        }
        static IEnumerable<int> GetSequence(int length)
        {
            for (int i = 0; i < length - 1; ++i)
            {
                yield return i;
            }
                
        }
        static void Main(string[] args)
        {
            List<int> seq = GetSequence(1000000).ToList();
            List<int> newSeq = TakeWithOut(seq, 1000).ToList();
            foreach (int i in newSeq)
                Console.Write("{0} ", i);
            Console.ReadKey();
        }
    }
}
