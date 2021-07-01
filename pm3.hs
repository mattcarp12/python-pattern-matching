
data Foo = Foobar String Int

foo_match :: Foo -> String
foo_match (Foobar "Hello" _) = "Hello Foo!"
foo_match (Foobar _ 42) = "Hello 42!"
foo_match (Foobar _ _) = "Foo Foo!"