{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE RecordWildCards #-}

module Lib
    ( scrape
    , popular
    , new
    ) where

import GHC.Generics
import Network.Wreq
import Data.Aeson
import Data.Aeson.Types
import Data.Aeson.Lens
import Control.Lens
import qualified Data.Text as T
import qualified Data.ByteString.Lazy as BL


-- | To ensure that urls done get used as regular text
newtype Url = Url T.Text deriving (Generic, FromJSON)

instance Show Url where
    show (Url t) = show t

-- | Defines the meme info we get from API
data Meme = Meme
    { displayName :: T.Text -- ^ "The Most Interesting Man In The World"
    , instanceID :: Int -- ^ 10574582
    , text0 :: T.Text -- ^ "i don\u0027t always use internet explorer..."
    , text1 :: T.Text -- ^ "but when i do, it\u0027s usually to download a better browser."
    , imageUrl :: Url -- ^ "https://cdn.meme.am/cache/images/folder485/400x/2485.jpg"
    } deriving (Show)


meme :: Value -> Parser Meme
meme = withObject "meme" $ \o -> do
       displayName <- o.:"displayName"
       instanceID <- o.:"instanceID"
       text0 <- o.:"text0"
       text1 <- o.:"text1"
       imageUrl <- o.:"imageUrl"
       return Meme{..}

popular = Url "http://version1.api.memegenerator.net/Instances_Select_ByPopular"
new = Url "http://version1.api.memegenerator.net/Instances_Select_ByNew"
    
scrape :: Url -> IO ()
scrape (Url address) = do
    r <- get (T.unpack address)
    case decode @Value (r ^. responseBody) of
      Just r' -> mapM_ (print . parseMaybe meme) (r' ^. key "result" . _Array)
      Nothing -> print "pull failed!"
