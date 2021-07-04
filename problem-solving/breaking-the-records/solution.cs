using System.Collections.Generic;

namespace ProblemSolving
{
    static class BreakingTheRecords
    {
        public static List<int> Solution(List<int> scores)
        {
            var highest = 0;
            var recordHighs = 0;
            var lowest = 0;
            var recordLows = 0;

            for (var i = 0; i < scores.Count; i++)
            {
                var score = scores[i];

                if (i == 0)
                {
                    highest = score;
                    lowest = score;
                }
                else if (score > highest)
                {
                    highest = score;
                    recordHighs++;
                }
                else if (score < lowest)
                {
                    lowest = score;
                    recordLows++;
                }
            }

            return new List<int> {recordHighs, recordLows};
        }
    }
}
