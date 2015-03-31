{-- Codes are based on a paper "Structuring Depth-First
Search Algorithm in Haskell", by King and Launchbury--}

----------- Data Structures and basic functions-------------------
import Data.Array

type Vertex = Char
type Table a = Array Vertex a
type Graph = Table [Vertex]

vertices :: Graph -> [Vertex]
vertices = indices

type Edge = (Vertex,Vertex)

edges :: Graph -> [Edge]
edges g = [(v,w) | v <- vertices g, w <- g!v]

mapT :: (Vertex -> a -> b) -> Table a -> Table b
mapT f t = array (bounds t)
				[(v, f v (t!v)) | v <- indices t]

type Bounds = (Vertex,Vertex)

outdegree :: Graph -> Table Int
outdegree g = mapT numEdge g
	where numEdge v ws = length ws

buildG :: Bounds -> [Edge] -> Graph
buildG bnds es = accumArray (flip (:)) [] bnds es

transposeG :: Graph -> Graph
transposeG g = buildG (bounds g) (reverseE g)

reverseE :: Graph -> [Edge]
reverseE g = [(w,v) |(v,w) <- edges g]

indegree :: Graph -> Table Int
indegree g = outdegree (transposeG g)

----------- DFS stuff--------------------------------------------
data Tree a = Node a (Forest a) deriving Show
type Forest a = [Tree a]

