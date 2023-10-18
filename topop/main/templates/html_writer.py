Tab_Title = ()
Title = ()
Detail = ()
Name = ()

f = open(f'{Name}.html', 'w')

# the html code which will go in the file html
html_template = f"""<html>
<head>
<title>{Tab_Title}</title>
</head>
<body>
<h2>{Title}</h2>

<p>{Detail}</p>

</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()
