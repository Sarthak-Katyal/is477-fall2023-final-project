rule prepare:
  output:
    "data/iris/iris.data"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data/iris/iris.data"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/iris/iris.data"
  output:
    "results/iris_pairplot_visualization.png"
  shell:
    "python scripts/analysis.py"
  
rule reproduce:
  input:
    "results/iris_pairplot_visualization.png",
    "profiling/report.html"