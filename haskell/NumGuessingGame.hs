{- A simple 'guess the random number' game: 
 - this demonstrates a use of I/O and,
 - more importantly, random numbers in Haskell.
 -}

import Char
import Data.Maybe
import System.Environment
import System.Exit
import System.Random

maxNum = 100

main :: IO ()
main = do
  args <- getArgs
  verifyArgsOrQuit args
  seed <- getSeed args
  showSeed seed
  playGame $ getRandomGen seed
  putStrLn "Game over"
	
-- create a random generator with the specified seed value
getRandomGen :: Int -> StdGen
getRandomGen seed = mkStdGen seed


-- If a seed is specified, use it; otherwise, pick a random one
-- This is a little ugly: a seed is initially in the form ["123"],
-- which is how it's represented as an argument to the program
getSeed :: [String] -> IO Int
getSeed [] = getRandomSeed
getSeed (x:_) = return $ read x

-- Use the pre-seeded random generator to get a random seed
-- for another random generator if none was specified by the user.
-- This is needed as I couldn't find a way to get the seed
-- out of an existing random generator (such as the system one),
-- yet I needed to be able to tell the user what the seed was,
-- so that the game would be repeatable.
getRandomSeed :: IO Int
getRandomSeed = do 
  randomSrc <- getStdGen
  return $ fst $ Random.random $ randomSrc

-- A top-level wrapper for actually playing the game.
playGame :: StdGen -> IO ()
playGame randomGen = do 
  putStrLn $ "\nGuess the number (between 0 and " ++ (show (maxNum - 1)) ++ ")"
  let (rawTargetNum, nextGen) = next randomGen
  let target = rawTargetNum `mod` maxNum
  guessFor target 0
  showAnswer target
  again <- playAgain
  if again
     then playGame nextGen
     else quitGame

-- guessFor handles all of the actual guesses during a game.
guessFor :: Int -> Int -> IO ()
guessFor target attempts =  do 
  putStr "Current guess? "
  guess <- getNum "\nCurrent guess? "
  if target == guess
     then guessCorrect $ attempts + 1
     else guessWrong target attempts guess 

guessCorrect :: Int -> IO ()
guessCorrect numTries = do 
  putStrLn $ "You won in " ++ show numTries ++ " guesses." 

guessWrong :: Int -> Int -> Int -> IO ()
guessWrong target attempts guess = do
  if target > guess
     then putStrLn "Too Low"
     else putStrLn "Too high"
  guessFor target $ attempts + 1

-- The rest of the code is I/O oriented: getting user input, 
-- and small wrappers to display stuff

-- Prompt until a valid Y / N (case-insensitive) is read, and return it.
getYN :: String -> IO Char
getYN promptAgain = 
  getFromStdin promptAgain getChar (`elem` "yYnN") toUpper

-- Prompt until a valid number is read, and return it
getNum :: String -> IO Int
getNum promptAgain = 
  getFromStdin promptAgain getLine isNum read

-- This contains the logic common to getNum and getYN;
-- it repeatedly prompts until input matching some criteria
-- is given, transforms that input, and returns it
getFromStdin :: String -> (IO a) -> (a -> Bool) -> (a -> b) -> IO b
getFromStdin promptAgain inputF isOk transformOk = do
  input <- inputF
  if isOk input
     then return $ transformOk input
     else do
       putStr promptAgain
       getFromStdin promptAgain inputF isOk transformOk



showSeed :: Int -> IO ()
showSeed seed = putStrLn $ "The random seed is " ++ show seed

showAnswer :: Int -> IO ()
showAnswer answer = putStrLn $ "The answer was " ++ show answer

-- Ask if the user wants to play again; 
-- getYN always returns an uppercase letter, so the check is sufficient
playAgain :: IO Bool
playAgain = do 
  putStr "Play again? "
  again <- getYN "\nPlay again? "
  return $ again == 'Y' 

quitGame :: IO ()
quitGame = do 
  putStrLn "\nEnough already."
  exitWith ExitSuccess


-- Argument verification code
verifyArgsOrQuit :: [String] -> IO ()
verifyArgsOrQuit args =
  if verifyArgs args
     then putStrLn "args ok!"
     else exitWithBadArgs

exitWithBadArgs :: IO ()
exitWithBadArgs = do 
  progName <- getProgName
  putStrLn $ "Use: " ++  progName ++ " [optional random seed]"
  exitWith $ ExitFailure 1

-- Legitimate arguments are none, or a string representing
-- a random seed.  Nothing else is accepted.
verifyArgs :: [String] -> Bool
verifyArgs [] = True
verifyArgs (x:xs) = null xs && isNum x

-- Verify that input is a number.  This approach was chosen as read raises an
-- exception if it can't parse its input.  This approach has the benefit
-- of being short, yet sufficient to allow the use of read on anything verified
-- with it, without having to deal with exceptions.
isNum :: String -> Bool
isnum [] = False 
isNum (x:xs) = all isDigit xs && (x == '-' || isDigit x)
