factorial    :: Int -> Int
factorial n  = foldl(\x y -> x * y) 1 ([1..n])
