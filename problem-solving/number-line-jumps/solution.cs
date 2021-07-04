namespace ProblemSolving
{
    class NumberLineJumps
    {
        private const string _YES = "YES";
        private const string _NO = "NO";

        public string Solution(int x1, int v1, int x2, int v2)
        {
            if (x1 == x2 && v1 == v2) return _YES;
            if (x1 > x2 && v1 > v2
                    || x1 < x2 && v1 < v2
                    || x1 == x2 && (v1 < v2 || v1 > v2))
                return _NO;

            if (x1 > x2) while (x1 > x2)
            {
                x1 += v1;
                x2 += v2;
            } if (x1 == x2) return _YES;

            if (x1 < x2) while (x1 < x2)
            {
                x1 += v1;
                x2 += v2;
            } if (x1 == x2) return _YES;

            return _NO;
        }
    }
}
