quicksort         :: [Int] -> [Int]
quicksort  []     =  []
quicksort (x:xs)  =  quicksort [y | y <- xs, y<x ]
                  ++ [x]
                  ++ quicksort [y | y <- xs, y>=x]

-- another version
{-

quicksort        :: [Int] -> [Int]
quicksort []     =  []
quicksort (x:xs) = quicksort small ++ pivot ++ quicksort large
   where
      small = [y | y<-xs, y<x]
      pivot = [y | y<-xs, y==x] ++ [x]
      large = [y | y<-xs, y>x]   

explanation for small: 'small' is the list of all y's such that y is drawn from the list xs, and y is less than x
-}
