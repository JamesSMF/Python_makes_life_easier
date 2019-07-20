-- divide and conquer: merge sort
sort :: (Ord a) => [a] -> [a]
sort [] = []
sort [x] = [x]
sort xs = merge (sort ys) (sort zs)
          where (ys, zs) = half xs

-- divide
half :: (Ord a) => [a] -> ([a], [a])
half xs = splitAt n xs
          where n = length xs `div` 2

-- conquer
merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) = if   x <= y then x:merge xs (y:ys)
                      else y:merge (x:xs) ys
