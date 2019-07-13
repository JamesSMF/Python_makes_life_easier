floor :: Float -> Integer
floor x = fst (until unit (shrink x) (bound x))
          where unit(m,n) = (m+1 == n)

type Interval = (Integer, Integer)

shrink :: Float -> Interval -> Interval
shrink x (m,n) = if fromInteger p <= x then (p,n) else (m,p)
                 where p = choose(m,n)

choose :: Interval -> Integer
choose(m,n) = (m+n) `div` 2

bound :: Float -> Interval
bound x = (lower x, upper x)

lower :: Float -> Integer
lower x = until (<= x) (*2) (-1)        -- double -1 until this value <= x

upper :: Float -> Integer
upper x = until (x <) (*2) 1            -- double 1 until x is less than this value
