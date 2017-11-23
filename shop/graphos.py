from graphos.sources.model import ModelDataSource
from models import Product
queryset = Account.objects.all()
data_source = ModelDataSource(queryset,
							  fields=['product', 'sales'])
chart = gchart.LineChart(html_id='gchart_div')

#PASSING THE VALUES TO JAVASCRIPT WHICH IS LOCATED IN GRAPHS.JS
#<script type="text/javascript" src="https://www.google.com/jsapi"></script>
#<script type="text/javascript">
#    google.load("visualization", "1", {packages:["corechart"]});
#</script>
#{{ chart.as_html }}
