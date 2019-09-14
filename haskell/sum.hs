sumList     :: [Int] -> Int
sumList xs  =  if      length xs == 1 then xs!!0
               else if null xs        then 0
               else                        xs!!0 + sumList (tail xs)

sumList2        :: [Int] -> Int
sumList2 []     = 0
sumList2 [x]    = x
sumList2 (x:xs) = x + sumList2 xs

sumList3        :: [Int] -> Int
sumList3 xs     = case xs of []      -> 0
                             [x]     -> x
                             (x:ys)  -> x + sumList3 ys

sumList4 :: [Int] -> Int
sumList4 xs
  | null xs        = 0
  | length xs == 1 = xs!!0
  | otherwise      = xs!!0 + sumList4 (tail xs)

sumList5    :: (Num a) => [a] -> a
sumList5 xs = foldl(\x y -> x + y) 0 (xs)

-- Alternatively you can omit xs
sumList6 :: (Num a) => [a] -> a
sumList6 = foldl(\x y -> x + y) 0
-- This will return a function that takes one parameter
