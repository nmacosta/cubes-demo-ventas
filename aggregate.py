import cubes

# 1. Prepare SQL data in memory
model = cubes.load_model("model.json")
workspace = cubes.create_workspace("sql", model,
                                   url='sqlite:///data.sqlite')

# 2. Create a model
cube = model.cube("bi_factur_resumen")

# 3. Create a browser and get a cell representing the whole cube (all data)
browser = workspace.browser(cube)
cell = cubes.Cell(cube)

# 4. Play with aggregates
result = browser.aggregate(cell)

print "Total\n" \
      "----------------------"

print "Record count: %8d" % result.summary["record_count"]
print "Total amount: %8d" % result.summary["valor_sum"]


#
# The End!
#
# ... of the Hello World! example
#
# The following is more than just plain "hello"... uncomment it all to the end.
#
#
# 5. Drill-down through a dimension
#
#
