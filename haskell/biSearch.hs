binsearch :: [Int] -> Int -> Int -> Int -> Int -- list, value, low, high, return int
binsearch xs value low high
   | high < low       = -1           -- Not found
   | xs!!mid > value  = binsearch xs value low (mid-1)      -- search lower half
   | xs!!mid < value  = binsearch xs value (mid+1) high     -- search upper half
   | otherwise        = mid          -- Found
   where
   mid = low + ((high - low) `div` 2)
