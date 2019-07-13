sumList     :: [Int] -> Int
sumList xs  =  if length xs == 1 then xs!!0
               else xs!!0 + sumList (tail xs)
