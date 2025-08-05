import os

# // 4.3 Recursive find: Write recursiveFind(), a callback-style function that
# // takes a path to a directory in the local filesystem and a keyword, as per the
# // following signature:
# // function recursiveFind(dir, keyword, cb) { /* ... */ }
# // The function must find all the text files within the given directory that
# // contain the given keyword in the file contents. The list of matching files
# // should be returned using the callback when the search is completed. If no
# // matching file is found, the callback must be invoked with an empty array.
# // As an example test case, if you have the files foo.txt, bar.txt, and baz.txt
# // in myDir and the keyword 'batman' is contained in the files foo.txt and baz.
# // txt, you should be able to run the following code:
# // recursiveFind('myDir', 'batman', console.log)
# // // should print ['foo.txt', 'baz.txt']
# // Bonus points if you make the search recursive (it looks for text files in any
# // subdirectory as well). Extra bonus points if you manage to perform the
# // search within different files and subdirectories in parallel, but be careful to
# // keep the number of parallel tasks under control!

def recursiveFind(dir, keyword, level):
    files = []

    def _find(dir, level): 
        try: 
            children = os.listdir(dir)
        except OSError as e: 
            print(f"Exception: {e}")

        if len(children) == 0:
            return
    
        for child in children:
            entry_path = os.path.join(dir, child)
            delimiter = "\t" * level
            ## print(f"{delimiter + child}")

            if os.path.isfile(entry_path):
                # if 'files' in locals():
                #     files.append(entry_path)
                # else:
                #     files = [entry_path]
                with open(entry_path, "r", encoding="latin-1") as f:
                    contents = f.read()
                    if keyword in contents:
                        files.append(child)
            elif os.path.isdir(entry_path):
                _find(entry_path, level + 1)

    _find(dir, level)
    return files


files = recursiveFind("/Users/alexforest/Desktop/AWS_Solutions_Architect", "api", 0)
for p in files:
    print(p)