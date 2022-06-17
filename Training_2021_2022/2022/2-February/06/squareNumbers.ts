const nums: number[] = [1,2,3]
let sol: number[] = []
sol = sortedSquares(nums)

function sortedSquares(nums: number[]): number[] {
    
    let res: number [] =[]
    for (let value of nums) {
        res.push(value**2)
    }
    res.sort()
    return res
};