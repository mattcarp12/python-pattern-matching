
sum1 :: [Int] -> Int
sum1 [] = 0
sum1 (x:xs) = x + (sum xs)