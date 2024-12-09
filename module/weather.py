import streamlit.components.v1 as components

code = """
<!-- weather widget start -->
<div id="m-booked-small-t1-43285">
 <div class="booked-weather-120x100 w100-bg" style="background-color:#FFFFFF; color:#333333; border-radius:4px; -moz-border-radius:4px; width:118px !important;">
   <div style="background-color:#2373CA; color:#FFFFFF;" class="booked-bl-simple-city">서울특별시</div> 
   <div class="booked-weather-120x100-degree w03"><span class="plus">+</span>1&deg;<sub class="booked-weather-120x100-type">C</sub></div> 
   <div class="booked-weather-120x100-high-low"> 
   <p>최고:: <span class="plus">+</span>4&deg;</p> 
   <p>최저:: -2&deg;</p> </div> <div style="background-color:#FFFFFF; color:#333333;" class="booked-weather-120x100-date">월, 09.12.2024</div> 
   </div> </div><script type="text/javascript"> var css_file=document.createElement("link"); var widgetUrl = location.href; css_file.setAttribute("rel","stylesheet"); css_file.setAttribute("type","text/css"); css_file.setAttribute("href",'https://s.bookcdn.com/css/w/bw-120-100.css?v=0.0.1'); document.getElementsByTagName("head")[0].appendChild(css_file); function setWidgetData_43285(data) { if(typeof(data) != 'undefined' && data.results.length > 0) { for(var i = 0; i < data.results.length; ++i) { var objMainBlock = document.getElementById('m-booked-small-t1-43285'); if(objMainBlock !== null) { var copyBlock = document.getElementById('m-bookew-weather-copy-'+data.results[i].widget_type); objMainBlock.innerHTML = data.results[i].html_code; if(copyBlock !== null) objMainBlock.appendChild(copyBlock); } } } else { alert('data=undefined||data.results is empty'); } } var widgetSrc = "https://widgets.booked.net/weather/info?action=get_weather_info;ver=6;cityID=18406;type=11;scode=;domid=593;anc_id=99742;cmetric=1;wlangID=24;color=ffffff;wwidth=118;header_color=2373ca;text_color=333333;link_color=ffffff;border_form=0;footer_color=ffffff;footer_text_color=333333;transparent=0";widgetSrc += ';ref=' + widgetUrl;widgetSrc += ';rand_id=43285';var weatherBookedScript = document.createElement("script"); weatherBookedScript.setAttribute("type", "text/javascript"); weatherBookedScript.src = widgetSrc; document.body.appendChild(weatherBookedScript) </script><!-- weather widget end -->
"""
def draw_weather():
    components.html(code, width=130, height=110)