const YES = "YES";
const NO = "NO";

const numberLineJumps = (x1, v1, x2, v2) => {
    if (x1 === x2 && v1 === v2)
        return YES;

    if (x1 > x2 && v1 > v2
            || x1 < x2 && v1 < v2
            || x1 === x2 && v1 !== v2)
        return NO;

    if (x1 > x2) while (x1 > x2)
    {
        x1 += v1;
        x2 += v2;
    }

    if (x1 === x2) return YES;

    if (x1 < x2) while (x1 < x2)
    {
        x1 += v1;
        x2 += v2;
    }

    if (x1 === x2) return YES;

    return NO;
}
