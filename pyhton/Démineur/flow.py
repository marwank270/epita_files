### Logigram making
from pyflowchart import FlowChart
with open('./demineur_v1.py') as f:
    code = f.read()
fc = FlowChart.from_code(code)
print(fc.FlowChart())