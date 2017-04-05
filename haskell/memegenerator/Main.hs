#!/usr/bin/env stack
{- stack
   script
   --resolver lts-8.5
   --package wreq
   --package aeson
   --package lens-aeson
   --package lens
   --package text
   --package bytestring
   --package optparse-generic
   --package time
-}

{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE RecordWildCards #-}

module Main where

import Options.Generic
import GHC.Generics
import Network.Wreq
import Control.Lens
import Data.Aeson
import Data.Aeson.Types
import Data.Aeson.Lens
import Data.Time.Clock.POSIX
import qualified Data.Text as T
import qualified Data.Text.IO as TIO
import qualified Data.Text.Lazy.Encoding as TE
import qualified Data.ByteString.Lazy as BL

data ScraperOptions = ScraperOptions
    { channel :: String -- ^ new | popular
    , outputFile :: String
    } deriving (Generic, ParseRecord)

-- | Defines the meme info we get from API
data Meme = Meme
    { title :: T.Text -- ^ "The Most Interesting Man In The World"
    , imageUrl :: T.Text -- ^ "https://cdn.meme.am/cache/images/folder485/400x/2485.jpg"
    , text0 :: Maybe T.Text -- ^ "i don\u0027t always use internet explorer..."
    , text1 :: Maybe T.Text -- ^ "but when i do, it\u0027s usually to download a better browser."
    , datePosted :: Maybe Integer
    , datePulled :: Maybe Integer
    } deriving (Generic, ToJSON)


meme :: Integer -> Value -> Parser Meme
meme time = withObject "meme" $ \o -> do
       title <- o.:"displayName"
       text0 <- o.:"text0"
       text1 <- o.:"text1"
       imageUrl <- o.:"imageUrl"
       datePulled <- return $ Just time
       datePosted <- return Nothing
       return Meme{..}

popular = "http://version1.api.memegenerator.net/Instances_Select_ByPopular"
new = "http://version1.api.memegenerator.net/Instances_Select_ByNew"


process :: FilePath -> Maybe Meme -> IO ()
process _ Nothing = return ()
process path (Just m) = BL.appendFile path (encode . toJSON $ m)

validateChannel :: ScraperOptions -> Maybe ScraperOptions
validateChannel (ScraperOptions c o)
    | c == "popular" = Just (ScraperOptions popular o)
    | c == "new" = Just (ScraperOptions new o)
    | otherwise = Nothing

scrape :: ScraperOptions -> IO ()
scrape (ScraperOptions url out) = do
    r <- get url
    t <- round <$> getPOSIXTime
    case decode @Value (r ^. responseBody) of
      Just r' -> mapM_ (process out . parseMaybe (meme t)) (r' ^. key "result" . _Array)
      Nothing -> print "pull failed!"

main :: IO ()
main = do
    opts <- getRecord "Memegenerator scraper"
    maybe (print "invalid channel") scrape (validateChannel opts)

