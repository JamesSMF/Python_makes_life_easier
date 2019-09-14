largestDiv :: (Integral a) => a
largestDiv = head (filter p [100000, 99999..])
    where p x = x `mod` 17 == 0
