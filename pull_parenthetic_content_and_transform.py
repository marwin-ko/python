# This code is a modification and extension of...
# https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level


def parenthetic_contents(string):
        """
        Pull parenthesized contents in string as dict where 
        keys is start/end indices and value is content.
        """
        pstack = []
        results = {}
        for i, c in enumerate(string):
            # parenthesis
            if c == '(':
                pstack.append(i)
            elif c == ')' and pstack:
                start = pstack.pop()
                content = string[start + 1: i]
                # TODO: find quotes
                # TODO: ignore brackets or parenthesis inside text field (e.g. "This (and that) is text field.")
                if not any([content.count(x) > 0 for x in '(){}']):
                    results[(start+1, i)] = content
        return dict(sorted(results.items(), reverse=True))
    
    def str_slice_replace(s, v, start, end):
        return s[:start] + v + s[end:]
    
    def transformer(v):
        # add transformer code
        return v
      
    def transform_all_content(s, d):
        for (start,end), v in d.items():
            s = str_slice_replace(s, transformer(v), start, end)
        return s
      
if __name__ == '__main__':
  # Assumes that all desired content is in parenthesis.
  # Use Case: To transform WHERE CLAUSE in SQL.
  
  s = '((f > 1) AND (f != 9)) OR (f IS NULL)'
  d = parenthetic_contents(s)
  new_s = replace_all_where_clauses(s,d)
  print(s)
  print(new_s)
