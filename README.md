
<div class=WordSection1>

# Task
Study the effects of four different heuristics on A* search of the Romania roadmap.

The heuristics are as follows, where (x1,y1 and (x2,y2) are the location so of the two cities

Heuristic #1: Straight Line Distance [ (x2-x1)^2 + (y2-y1)^2)^1/2

Heuristic #2: Manhattan Distance (x2-x1)+(y2-y1)

Heuristic #3: Sum of first two heuristics

Heuristic #4: Average of first two heuristics

1. Write a python program that implements A* search for the snippet of the roadmap we did in class

2. Select a set of 10 city pairs on the map, where there are multiple routes for each pair (as in Arad, Bucharest), and establish the optimal path by hand between each pair.

3. Evaluate A* using each heuristic on all 10 pairs, and count the number of optimal paths returned

4. Plot your results

5. Write a document with two sections. In the first section, document your code. In the second section, include your plot and explain  in detail your results. Are there any general conclusions you can draw?


<p class=MsoNormal><span class=GramE><b><span style='font-size:16.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Author :</span></b></span><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> Chengpi Wu<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>Section</span></b><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> </span></b><b><span style='font-size:16.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>1 AstarSearch.py<o:p></o:p></span></b></p>



<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>Section</span></b><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> </span></b><b><span style='font-size:16.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>2 Results and
analysis<o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>In order to compare the results of the
same pairs easily, I adjusted the orders of graphs.</span><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin;mso-no-proof:yes'><!--[if gte vml 1]><v:shapetype
 id="_x0000_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t"
 path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="Picture_x0020_141" o:spid="_x0000_i1104" type="#_x0000_t75"
 style='width:271.2pt;height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image001.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image002.png" v:shapes="Picture_x0020_141"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_142" o:spid="_x0000_i1103" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image003.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image004.png" v:shapes="Picture_x0020_142"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_143" o:spid="_x0000_i1102" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image005.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image006.png" v:shapes="Picture_x0020_143"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_144" o:spid="_x0000_i1101" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image007.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image008.png" v:shapes="Picture_x0020_144"><![endif]></span></b><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

</div>

<b><span style='font-size:16.0pt;line-height:107%;font-family:"Calibri",sans-serif;
mso-ascii-theme-font:minor-latin;"Microsoft Yi Baiti";
mso-fareast-theme-font:minor-fareast;mso-hansi-theme-font:minor-latin;
mso-bidi-theme-font:minor-latin;mso-ansi-language:EN-US;
KO;mso-bidi-language:AR-SA'><br clear=all style='page-break-before:always;
mso-break-type:section-break'>
</span></b>

<div class=WordSection2>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Picture_x0020_145" o:spid="_x0000_i1100" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image009.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image010.png" v:shapes="Picture_x0020_145"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_146" o:spid="_x0000_i1099" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image011.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image012.png" v:shapes="Picture_x0020_146"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_147" o:spid="_x0000_i1098" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image013.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image014.png" v:shapes="Picture_x0020_147"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_148" o:spid="_x0000_i1097" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image015.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image016.png" v:shapes="Picture_x0020_148"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_149" o:spid="_x0000_i1096" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image017.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image018.png" v:shapes="Picture_x0020_149"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_150" o:spid="_x0000_i1095" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image019.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image020.png" v:shapes="Picture_x0020_150"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_151" o:spid="_x0000_i1094" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image021.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image022.png" v:shapes="Picture_x0020_151"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_152" o:spid="_x0000_i1093" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image023.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image024.png" v:shapes="Picture_x0020_152"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_153" o:spid="_x0000_i1092" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image025.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image026.png" v:shapes="Picture_x0020_153"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_154" o:spid="_x0000_i1091" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image027.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image028.png" v:shapes="Picture_x0020_154"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_155" o:spid="_x0000_i1090" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image029.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image030.png" v:shapes="Picture_x0020_155"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_156" o:spid="_x0000_i1089" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image031.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image032.png" v:shapes="Picture_x0020_156"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_157" o:spid="_x0000_i1088" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image033.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image034.png" v:shapes="Picture_x0020_157"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_158" o:spid="_x0000_i1087" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image035.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image036.png" v:shapes="Picture_x0020_158"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_159" o:spid="_x0000_i1086" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image037.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image038.png" v:shapes="Picture_x0020_159"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_160" o:spid="_x0000_i1085" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image039.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image040.png" v:shapes="Picture_x0020_160"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_161" o:spid="_x0000_i1084" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image041.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image042.png" v:shapes="Picture_x0020_161"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_162" o:spid="_x0000_i1083" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image043.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image044.png" v:shapes="Picture_x0020_162"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_163" o:spid="_x0000_i1082" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image045.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image046.png" v:shapes="Picture_x0020_163"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_164" o:spid="_x0000_i1081" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image047.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image048.png" v:shapes="Picture_x0020_164"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_165" o:spid="_x0000_i1080" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image049.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image050.png" v:shapes="Picture_x0020_165"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_166" o:spid="_x0000_i1079" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image051.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image052.png" v:shapes="Picture_x0020_166"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_167" o:spid="_x0000_i1078" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image053.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image054.png" v:shapes="Picture_x0020_167"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_168" o:spid="_x0000_i1077" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image055.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image056.png" v:shapes="Picture_x0020_168"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_169" o:spid="_x0000_i1076" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image057.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image058.png" v:shapes="Picture_x0020_169"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_170" o:spid="_x0000_i1075" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image059.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image060.png" v:shapes="Picture_x0020_170"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_171" o:spid="_x0000_i1074" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image061.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image062.png" v:shapes="Picture_x0020_171"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_172" o:spid="_x0000_i1073" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image063.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image064.png" v:shapes="Picture_x0020_172"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_173" o:spid="_x0000_i1072" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image065.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image066.png" v:shapes="Picture_x0020_173"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_174" o:spid="_x0000_i1071" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image067.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image068.png" v:shapes="Picture_x0020_174"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_175" o:spid="_x0000_i1070" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image069.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image070.png" v:shapes="Picture_x0020_175"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_176" o:spid="_x0000_i1069" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image071.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image072.png" v:shapes="Picture_x0020_176"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_177" o:spid="_x0000_i1068" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image073.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image074.png" v:shapes="Picture_x0020_177"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_178" o:spid="_x0000_i1067" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image075.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image076.png" v:shapes="Picture_x0020_178"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_179" o:spid="_x0000_i1066" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image077.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image078.png" v:shapes="Picture_x0020_179"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_180" o:spid="_x0000_i1065" type="#_x0000_t75" style='width:271.2pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image079.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=362 height=278
src="AstarSearch_Readme_images/image080.png" v:shapes="Picture_x0020_180"><![endif]></span></b><b><span
style='font-size:16.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

</div>

<b><span style='font-size:16.0pt;line-height:107%;font-family:"Calibri",sans-serif;
mso-ascii-theme-font:minor-latin;"Microsoft Yi Baiti";
mso-fareast-theme-font:minor-fareast;mso-hansi-theme-font:minor-latin;
mso-bidi-theme-font:minor-latin;mso-ansi-language:EN-US;
KO;mso-bidi-language:AR-SA'><br clear=all style='page-break-before:always;
mso-break-type:section-break'>
</span></b>

<div class=WordSection3>

<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>1.By the A* search code, we could find
out that in some cases it could not generate the optimal paths because the
heuristic function defined is not admissible. <span class=GramE>( pair</span>
3, heuristic #3 ; pair 7, #1, #2, #4; pair 8, #2, #3; pair 9, #3</span><span
style='font-size:12.0pt;line-height:107%;宋体;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>)</span><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>2.In some cases, we could get the
optimal paths with different heuristic functions though the numbers of steps
are different. (for example, pair 10, #<span class=GramE>1,#</span>2,#3,#4 have
7,4,4,5 steps respectively.)<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>3.Why can’t the search algorithm find
the optimal routes in some cases? Because the h(n) with the multiplier (or <span
style='color:red'>ratio scale, I guess it’s the real meaning of the multiplier</span>)
25 sometimes would overestimate the cost to the goal, so it’s not admissible.
Then the result wouldn’t be optimal.<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>4.By improving A* search code, I got
the same paths in each pair of cities with different heuristic functions. And
we can check these results are all optimal paths.<span
style='mso-spacerun:yes'>  </span>(Please find the improved code and its result
at the end.)<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>5.In my new code, I used different so-called
“ratio <span class=GramE>scales”(</span>multipliers) defined by the smallest ratio
of the length of real route to the “distance”(straight line distance, Manhattan
distance, sum and average).<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>I used several functions to calculate
ratio scales for each definition of cost instead of the value 25 which Prof.
Lyons suggest us to use. <o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>For example:<o:p></o:p></span></p>

<p class=MsoNormal><span class=SpellE><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>scaleSld</span></span><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> (): calculate smallest ratio of length of
real route between two cities to the <span class=GramE>straight line</span>
distance between two cities<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>And I define a dictionary named <span
class=SpellE>disDic</span> to save the method’s name, description and ratio
scales for each <span class=SpellE>heurisitic</span> function.<o:p></o:p></span></p>

<p class=MsoNormal><span class=SpellE><span style='font-size:12.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>disDic</span></span><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> = {'<span class=SpellE>sld</span>':('Heuristic
#1: Straight Line Distance<span class=GramE>',<span class=SpellE>scaleSld</span></span>),etc.}<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>In the method of <span class=SpellE>ASTARtreesearch</span>(<span
class=SpellE><span class=GramE>start,goal</span>,heuristic</span>), I calculate
F(n) =g(n) + h(n) by: <o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>h = <span class=SpellE>globals</span><span
class=GramE>()[</span>heuristic](<span class=SpellE>city,goal</span>) * <span
class=SpellE>ratioScale</span>, </span><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>where <span class=SpellE>ratioScale</span>
= <span class=SpellE>disDic.get</span>(heuristic<span class=GramE>)[</span>1]<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>Based on the given map data, I got 4
values of ratio scale for different distance we defined:<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>Ratio Scale of <span
class=SpellE>sld</span> = 23.43<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>Ratio Scale of md = 17.64<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>Ratio Scale of <span
class=SpellE>sumsldmd</span> = 10.06<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>Ratio Scale of <span
class=SpellE>avgsldmd</span> = 20.12<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>Notice the Ratio Scale of <span
class=SpellE>sld</span> (straight line distance) is very close to the value 25,
however, the other ratio scale values are smaller, which could ensure that h(n)&lt;h*(n)
so that h(n) could be admissible (however, the function is not strictly
admissible theoretically, I will discuss that as follows).<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>6. Construct a good h(n) (estimating
ratio scale in this case) is challenging. First, if h(n) can’t satisfy the
condition h(n)&lt;h*(n), h(n) is not admissible and A* search would not be
optimal. Second, if the heuristic function underestimates the cost to the goal
too much, the A* search would be inefficient because the algorithm has to
expand many nodes with smaller h(n) but bigger g(n) (which means we give a
bigger weight to the cost so far in the estimation). <o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>It could be seen that all the
h(n)=distance*(ratio scale) could cause to the optimal paths, though they take
different steps in some cases. In this case, for pair 2 and 7, heuristic
function of adjusted straight line distance takes least steps (the others are
the same) (for example, in the results of the improved code, for pair7,
heuristic #1 has 10 steps though #2,#3,#4 have 11 steps); for pair 8,9,10,
heuristic function of adjusted straight line distance takes most steps (the
others are the same).<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>All though the ratio scales(multipliers)
of different distances I calculated do work in this case, it is not strictly
admissible because the condition h(n)&lt;h*(n) can’t be satisfied in any cases.
</span><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>(Although for any between two
connected cities nearby, the adjusted distance &lt; the length of real route,
for two cities not connected directly, <span style='color:red'>the inequality </span></span><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:red'>doesn’t
follow sigma additivity strictly</span><span style='font-size:12.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>.)</span><span
style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'> However, it is acceptable in most cases, or
it’s good enough as an estimate.<o:p></o:p></span></p>

<p class=MsoNormal><b><span style='font-size:12.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;color:red'>7.
Conclusion: <o:p></o:p></span></b></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>A* search is optimal if we could
define heuristic function correctly. (h(n) satisfy the condition h(n)&lt;h*(n),
where h*(n) is the real cost to the goal, and the h(n) don’t underestimate too
much).<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>Through different but admissible heuristic
functions (h(n)=distance*(ratio scale)), we could get the same optimal paths
even if we use different heuristic functions. The less h(n) underestimate, the
more efficient the algorithm is. <o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>8. The improved code and its result
are as follows:<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:12.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>ASTAR_ratioScale.py<o:p></o:p></span></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>###############################################<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>Created on Thu <span class=GramE>Sep<span style='mso-spacerun:yes'> 
</span>15</span> 19:02:04 2020<span style='mso-spacerun:yes'>    </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>      
</span>Assignment #1:<span style='mso-spacerun:yes'>    </span>Chengpi Wu<span
style='mso-spacerun:yes'>          </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>###############################################<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#Part of the <span class=SpellE>romania</span>
<span class=SpellE>roadmapp</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>roadmap =
[(&quot;arad&quot;,&quot;zerind&quot;,75),
(&quot;arad&quot;,&quot;sibiu&quot;,140<span class=GramE>),(</span>&quot;arad&quot;,&quot;timisoara&quot;,118),(&quot;zerind&quot;,&quot;oradea&quot;,71),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>      
</span>(&quot;oradea&quot;,&quot;sibiu&quot;,151<span class=GramE>),(</span>&quot;timisoara&quot;,&quot;lugoj&quot;,111),(&quot;lugoj&quot;,&quot;mehadia&quot;,70),(&quot;mehadia&quot;,&quot;drobeta&quot;,75),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>      
</span>(&quot;drobeta&quot;,&quot;craiova&quot;,120<span class=GramE>),(</span>&quot;craiova&quot;,&quot;rimnicu&quot;,146),(&quot;rimnicu&quot;,&quot;sibiu&quot;,80),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>      
</span>(&quot;craiova&quot;,&quot;pitesti&quot;,138<span class=GramE>),(</span>&quot;rimnicu&quot;,&quot;pitesti&quot;,97),(&quot;sibiu&quot;,&quot;fagaras&quot;,99),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>      
</span>(&quot;pitesti&quot;,&quot;bucharest&quot;,101),
(&quot;fagaras&quot;,&quot;bucharest&quot;,211),
(&quot;giurgiu&quot;,&quot;bucharest&quot;,90)]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>location={&quot;<span class=SpellE>arad</span>&quot;:(1.75,10.75),
&quot;<span class=SpellE>zerind</span>&quot;:(2.5,12.5), &quot;<span
class=SpellE>sibiu</span>&quot;:(6.75,9.25),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>          </span>&quot;<span class=SpellE>timisoara</span>&quot;:(1.75,7),
&quot;<span class=SpellE>oradea</span>&quot;:(3.3,14), &quot;<span
class=SpellE>lugoj</span>&quot;:(4.8,5.8),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>          </span>&quot;<span class=SpellE>mehadia</span>&quot;:(5,4),
&quot;<span class=SpellE>drobeta</span>&quot;:(4.8,2.5), &quot;<span
class=SpellE>craiova</span>&quot;:(8.75,1.75),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>          </span>&quot;<span class=SpellE>rimnicu</span>&quot;:(8,7),
&quot;<span class=SpellE>fagaras</span>&quot;:(10.5, 9), &quot;<span
class=SpellE>pitesti</span>&quot;:(11.75,5.25),<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>          </span>&quot;<span class=SpellE>bucharest</span>&quot;:(15,3.5),
&quot;<span class=SpellE>giurgiu</span>&quot;:(14,1<span class=GramE>) }</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># Successor <span class=SpellE>fn</span>:
successor(<span class=SpellE><span class=GramE>state,action</span></span>)=list
of states arrived at after action in state<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def successor(<span class=SpellE><span
class=GramE>roadmap,city</span></span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>&quot;&quot;&quot;generate list of successors of <span class=SpellE>startcity</span>
in roadmap&quot;&quot;&quot;<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span># assumes format of roadmap and that city is a strong<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>successorList</span><span class=GramE>=[</span>]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>mapentry</span> in roadmap:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if <span class=SpellE><span class=GramE>mapentry</span></span><span
class=GramE>[</span>0]==city:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>successorList.append</span><span
class=GramE>( (</span><span class=SpellE>mapentry</span>[1], <span
class=SpellE>mapentry</span>[2]) )<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>elif</span> <span class=SpellE><span class=GramE>mapentry</span></span><span
class=GramE>[</span>1]==city:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>successorList.append</span><span
class=GramE>( (</span><span class=SpellE>mapentry</span>[0], <span
class=SpellE>mapentry</span>[2]) )<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return <span class=SpellE>successorList</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>'\n-----------------
ASTAR search -------------------\n')<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>import math<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># define <span class=SpellE>diffrent</span>
&quot;distances&quot;<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE>sld</span>(<span
class=GramE>X,Y</span>):<span style='mso-spacerun:yes'>  </span>#1: Straight
Line Distance<span style='mso-spacerun:yes'>  </span>[ (x2-x1)^2 +
(y2-y1)^2)^1/2<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(<span class=SpellE><span class=GramE>math.sqrt</span></span>((location[Y][0]-location[X][0])**2
+<span style='mso-spacerun:yes'>  </span>(location[Y][1]-location[X][1])**2) ,
2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def md(<span class=GramE>X,Y</span>):<span
style='mso-spacerun:yes'>   </span>#2: Manhattan Distance (x2-x1)+(y2-y1)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(abs(location[Y][0]-location[X][0]) <span class=GramE>+<span
style='mso-spacerun:yes'>  </span>abs</span>(location[Y][1]-location[X][1]) ,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE>sumsldmd</span>(<span
class=GramE>X,Y</span>):#3: Sum of first two heuristics<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return <span class=SpellE>sld</span>(<span class=GramE>X,Y</span>) +
md(X,Y)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE>avgsldmd</span>(<span
class=GramE>X,Y</span>):#4: Average of first two heuristics<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round((<span class=SpellE>sld</span>(<span class=GramE>X,Y</span>)
+ md(X,Y))/2,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'> 
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># calculate scale ratio as the
multiplier of distance - begin<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># calculate smallest ratio of length of
real route/<span class=SpellE>Sld</span> between two cities<span
style='mso-spacerun:yes'>     </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>scaleSld</span></span><span class=GramE>(</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>minRatio</span> = 999999<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span> in range(<span class=GramE>0,len</span>(roadmap)):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>ratio = roadmap[<span class=SpellE>i</span>][2]/<span class=SpellE>sld</span>(roadmap[<span
class=SpellE>i</span>][0<span class=GramE>],roadmap</span>[<span class=SpellE>i</span>][1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if ratio &lt; <span class=SpellE>minRatio</span>:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>minRatio</span>
= ratio<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(minRatio,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># calculate smallest ratio of length of
real route/<span class=GramE>Md<span style='mso-spacerun:yes'>  </span>between</span>
two cities<span style='mso-spacerun:yes'>   </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>scaleMd</span></span><span class=GramE>(</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>minRatio</span> = 999999<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span> in range(<span class=GramE>0,len</span>(roadmap)):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>ratio = roadmap[<span class=SpellE>i</span>][2]/md(roadmap[<span
class=SpellE>i</span>][0<span class=GramE>],roadmap</span>[<span class=SpellE>i</span>][1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if ratio &lt; <span class=SpellE>minRatio</span>:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>minRatio</span>
= ratio<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(minRatio,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># calculate smallest ratio of length of
real route<span class=GramE>/(</span>sum of <span class=SpellE>Sld</span> and
Md) between two cities<span style='mso-spacerun:yes'>    </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>scaleSumsldmd</span></span><span class=GramE>(</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>minRatio</span> = 999999<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span> in range(<span class=GramE>0,len</span>(roadmap)):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>ratio = roadmap[<span class=SpellE>i</span>][2]/<span class=SpellE>sumsldmd</span>(roadmap[<span
class=SpellE>i</span>][0<span class=GramE>],roadmap</span>[<span class=SpellE>i</span>][1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if ratio &lt; <span class=SpellE>minRatio</span>:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>minRatio</span>
= ratio<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(minRatio,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># calculate smallest ratio of length of
real route<span class=GramE>/(</span>average of <span class=SpellE>Sld</span>
and Md) between two cities <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>scaleAvgsldmd</span></span><span class=GramE>(</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>minRatio</span> = 999999<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span> in range(<span class=GramE>0,len</span>(roadmap)):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>ratio = roadmap[<span class=SpellE>i</span>][2]/<span class=SpellE>avgsldmd</span>(roadmap[<span
class=SpellE>i</span>][0<span class=GramE>],roadmap</span>[<span class=SpellE>i</span>][1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if ratio &lt; <span class=SpellE>minRatio</span>:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE>minRatio</span>
= ratio<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>return round(minRatio,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>          </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># assign 4 ratio scales as the
multiplier of distance<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>scaleSld</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = <span
class=SpellE><span class=GramE>scaleSld</span></span><span class=GramE>(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>scaleMd</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = <span
class=SpellE><span class=GramE>scaleMd</span></span><span class=GramE>(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>scaleSumsldmd</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = <span
class=SpellE><span class=GramE>scaleSumsldmd</span></span><span class=GramE>(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>scaleAvgsldmd</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = <span
class=SpellE><span class=GramE>scaleAvgsldmd</span></span><span class=GramE>(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;Ratio
Scale of <span class=SpellE>sld</span> =&quot;,<span class=SpellE>scaleSld</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;Ratio
Scale of md =&quot;,<span class=SpellE>scaleMd</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;Ratio
Scale of <span class=SpellE>sumsldmd</span> =&quot;,<span class=SpellE>scaleSumsldmd</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;Ratio
Scale of <span class=SpellE>avgsldmd</span> =&quot;,<span class=SpellE>scaleAvgsldmd</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>####################################################<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span
style='mso-spacerun:yes'>          </span>calculate scale ratio - end<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>disDic</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = {'<span
class=SpellE>sld</span>':('Heuristic #1: Straight Line Distance<span
class=GramE>',<span class=SpellE>scaleSld</span></span>),'md':('Heuristic #2:
Manhattan Distance',<span class=SpellE>scaleMd</span>), <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>              </span>'<span class=SpellE>sumsldmd</span>':('Heuristic
#3: Sum of first two heuristics<span class=GramE>',<span class=SpellE>scaleSumsldmd</span></span>),'<span
class=SpellE>avgsldmd</span>':('Heuristic #4: Average of first two heuristics',<span
class=SpellE>scaleAvgsldmd</span>)}<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE>ASTARtreesearch</span>(<span
class=SpellE><span class=GramE>start,goal</span>,heuristic</span>): # not
finished! <span class=SpellE>everytime</span> just search the shortest branch!<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>&quot;&quot;&quot;carry out a tree search for goal from this fringe (set
of unexpanded nodes to search)&quot;&quot;&quot;<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span># assumes that the start state is in the fringe<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=GramE>print(</span>&quot;\n\n##### &quot;,<span
class=SpellE>disDic.get</span>(heuristic)[0],&quot;#####\n&quot;)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>ratioScale</span> = <span class=SpellE>disDic.get</span>(heuristic<span
class=GramE>)[</span>1]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>rubbish = <span class=GramE>list(</span>) # list of already <span
class=SpellE>seached</span> cities<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>routes = <span class=GramE>list(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>fringe = [ [<span class=GramE>start,[</span>], 0, round(<span
class=SpellE>globals</span>()[heuristic](<span class=SpellE>start,goal</span>)*<span
class=SpellE>ratioScale</span> ,2)] ]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>steps = 0<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>while <span class=SpellE>len</span>(fringe)&gt;0:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>fringe = <span class=GramE>sorted(</span><span class=SpellE>fringe,key</span>=lambda
x:(x[3]))<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>rootnode</span> = <span class=SpellE><span
class=GramE>fringe.pop</span></span><span class=GramE>(</span>0) # <span
class=SpellE>thisis</span> the strategy - just pick the first one<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>root = <span class=SpellE><span class=GramE>rootnode</span></span><span
class=GramE>[</span>0]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>if root == goal:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>print ('\<span class=SpellE>nFound</span>
goal and the route is: \n<span class=GramE>',<span class=SpellE>rootnode</span></span>[1]+[goal],
'\n length: ', <span class=SpellE>rootnode</span>[2] ,'\<span class=SpellE>nsteps</span>:
',steps,'\n')<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE><span
class=GramE>routes.append</span></span>([<span class=SpellE>rootnode</span>[1]+[goal],<span
class=SpellE>rootnode</span>[2]])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>return <span class=SpellE>rootnode</span>[<span
class=GramE>1]+</span>[goal],<span class=SpellE>rootnode</span>[2],steps<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>nextcitylist</span> = successor(<span class=SpellE><span
class=GramE>roadmap,root</span></span>) # assumes global scope roadmap<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>rubbish.append</span></span>(root)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>#<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>fringecity</span>=<span class=GramE>list(</span>) #
can't check fringe directly for duplicates so extract cities to list<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'> </span><span
style='mso-spacerun:yes'>       </span>for <span class=SpellE>searchnode</span>
in fringe:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span><span class=SpellE><span
class=GramE>fringecity.append</span></span>(<span class=SpellE>searchnode</span>[0])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>#ASTAR<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>steps += 1<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span># <span class=GramE>print(</span>'ASTAR search: ', root, round(<span
class=SpellE>rootnode</span>[3],2))<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span># print(<span class=SpellE>nextcitylist</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>for <span class=SpellE>mapentry</span> in <span class=SpellE>nextcitylist</span>:
<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>city = <span class=SpellE><span
class=GramE>mapentry</span></span><span class=GramE>[</span>0]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>g = <span class=SpellE><span
class=GramE>rootnode</span></span><span class=GramE>[</span>2] # cost happened<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span># h = <span class=SpellE>sld</span>(<span
class=SpellE><span class=GramE>city,goal</span></span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>h = <span class=GramE>round( <span
class=SpellE>globals</span></span>()[heuristic](<span class=SpellE>city,goal</span>)
* <span class=SpellE>ratioScale</span> ,2)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>f = g + h<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>length = <span class=SpellE><span
class=GramE>rootnode</span></span><span class=GramE>[</span>2] + <span
class=SpellE>mapentry</span>[1]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>            </span>if not city in <span class=SpellE>fringecity</span>
and not city in rubbish or city == goal: # <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>                </span><span class=SpellE>newnode</span>=[<span
class=SpellE><span class=GramE>city,rootnode</span></span>[1]+[root], length,
f] # expand the path by one city<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>                </span><span class=SpellE><span
class=GramE>fringe.append</span></span>(<span class=SpellE>newnode</span>)# put
them at the end<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>if routes:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>return routes<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>else:<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>return &quot;No route to &quot;+goal<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>define a city pairs list<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>pairsCity</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = [('<span
class=SpellE>drobeta</span>', '<span class=SpellE>zerind</span>'), ('<span
class=SpellE>fagaras</span>', '<span class=SpellE>mehadia</span>'), ('<span
class=SpellE>timisoara</span>', '<span class=SpellE>bucharest</span>'), ('<span
class=SpellE>bucharest</span>', '<span class=SpellE>mehadia</span>'), <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>             </span>('<span class=SpellE>bucharest</span>',
'<span class=SpellE>zerind</span>'), ('<span class=SpellE>oradea</span>', '<span
class=SpellE>drobeta</span>'), ('<span class=SpellE>rimnicu</span>', '<span
class=SpellE>lugoj</span>'), ('<span class=SpellE>timisoara</span>', '<span
class=SpellE>giurgiu</span>'), <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>             </span>('<span class=SpellE>lugoj</span>',
'<span class=SpellE>fagaras</span>'), ('<span class=SpellE>zerind</span>', '<span
class=SpellE>craiova</span>')]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>  
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;\<span
class=SpellE>nCity</span> pairs: \n&quot;,<span class=SpellE>pairsCity</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span class=GramE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>print(</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>&quot;\n\n-----
Plot optimal paths -----\n&quot;)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>import <span class=SpellE><span
class=GramE>matplotlib.pyplot</span></span> as <span class=SpellE>plt</span> <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'># convert the coordinate to a list to
plot<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>coord</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = <span
class=SpellE><span class=GramE>location.values</span></span>()<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>cityCoordlist</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> =
list(zip(*<span class=SpellE>coord</span>))<o:p></o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>cityCoordinate</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = [list(x)
for x in <span class=SpellE>cityCoordlist</span>]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span class=SpellE><b><span style='font-size:10.0pt;
line-height:107%;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>cityList</span></b></span><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'> = list(<span
class=SpellE><span class=GramE>location.keys</span></span>())<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw original map - begin<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>drawMap</span></span><span class=GramE>(</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE><span class=GramE>plt.axis</span></span>([0, 18, 0,
16]) <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span># naming the x axis <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE><span class=GramE>plt.xlabel</span></span>('x -
axis') <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span># naming the y axis <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE><span class=GramE>plt.ylabel</span></span>('y -
axis')<span style='mso-spacerun:yes'>     </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span>, txt in enumerate(<span class=SpellE>cityList</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>plt.annotate</span></span>(txt, (<span
class=SpellE>cityCoordinate</span>[0][<span class=SpellE>i</span>]+0.2, <span
class=SpellE>cityCoordinate</span>[1][<span class=SpellE>i</span>]+0.2))<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE><span class=GramE>i,pair</span></span> in
enumerate(roadmap):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=GramE>plt.plot</span>([location[roadmap[i][0]][0],location[roadmap[i][1]][0]],
[location[roadmap[<span class=SpellE>i</span>][0]][1],location[roadmap[<span
class=SpellE>i</span>][1]][1]], marker = 'o', <span class=SpellE>linestyle</span>=':')<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw original map - end<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw optimal route - begin<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE><span
class=GramE>drawArrow</span></span><span class=GramE>(</span><span
class=SpellE>cityA</span>, <span class=SpellE>cityB</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE>location.get</span>(<span class=SpellE>cityA</span><span
class=GramE>)[</span>0]<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=GramE>plt.plot</span>([location.get(cityA)[0],location.get(cityB)[0]],[location.get(cityA)[1],location.get(cityB)[1]],
marker = 'o', color='red')<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span><span class=SpellE><span class=GramE>plt.arrow</span></span>(<span
class=SpellE>location.get</span>(<span class=SpellE>cityA</span>)[0],<span
class=SpellE>location.get</span>(<span class=SpellE>cityA</span>)[1], <span
class=SpellE>location.get</span>(<span class=SpellE>cityB</span>)[0] - <span
class=SpellE>location.get</span>(<span class=SpellE>cityA</span>)[0], <span
class=SpellE>location.get</span>(<span class=SpellE>cityB</span>)[1] - <span
class=SpellE>location.get</span>(<span class=SpellE>cityA</span>)[1],<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span
style='mso-spacerun:yes'>              </span><span class=SpellE>head_width</span>=0.6,
<span class=SpellE>length_includes_head</span>=<span class=SpellE><span
class=GramE>True,color</span></span>='red')<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>def <span class=SpellE>drawRoute</span>(<span
class=SpellE>routeList</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>i</span> in range(<span class=GramE>0,len</span>(<span
class=SpellE>routeList</span>)-1):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>drawArrow</span>(<span class=SpellE>routeList</span>[<span
class=SpellE>i</span><span class=GramE>],<span class=SpellE>routeList</span></span>[i+1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw optimal route - end<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'> 
</span><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw optimal route of 10 pairs - begin<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>for <span class=SpellE><span
class=GramE>i,pair</span></span> in enumerate(<span class=SpellE>pairsCity</span>):<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>   
</span>for <span class=SpellE>numHeur</span> in <span class=GramE>range(</span>1,5):
# run all heuristics.<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span>fig = <span class=SpellE><span class=GramE>plt.figure</span></span>(<span
class=SpellE>figsize</span>=(10, 7))<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=GramE>print(</span>&quot;----- pair &quot;,i+1,pair,&quot;
-----&quot;)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>drawMap</span></span><span
class=GramE>(</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>routeResult,length</span>,steps</span>
= <span class=SpellE>ASTARtreesearch</span>(pair[0],pair[1],list(<span
class=SpellE>disDic.keys</span>())[numHeur-1])<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE>drawRoute</span>(<span class=SpellE>routeResult</span>)<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span># giving a title to the graph <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>plt.title</span></span>(list(<span
class=SpellE>disDic.values</span>())[numHeur-1][0] +'\<span class=SpellE>nA</span>*
optimal path between\<span class=SpellE>npair</span>' + &quot; &quot; +
str(i+1) + &quot;: &quot; + pair[0] + ' - ' + pair[1] + ' length:' +
str(length) + ' steps:' + str(steps)) <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>plt.show</span></span>() <o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><span style='mso-spacerun:yes'>       
</span><span class=SpellE><span class=GramE>plt.close</span></span>()<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'>#<span style='mso-spacerun:yes'>    
</span>draw optimal route of 10 pairs - end<o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;mso-no-proof:
yes'><!--[if gte vml 1]><v:shape id="Picture_x0020_81" o:spid="_x0000_i1064"
 type="#_x0000_t75" style='width:276.6pt;height:208.8pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image001.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image081.png" v:shapes="Picture_x0020_81"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_82" o:spid="_x0000_i1063" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image082.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image083.png" v:shapes="Picture_x0020_82"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_83" o:spid="_x0000_i1062" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image084.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image085.png" v:shapes="Picture_x0020_83"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_84" o:spid="_x0000_i1061" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image007.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image086.png" v:shapes="Picture_x0020_84"><![endif]></span></b><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

</div>

<b><span style='font-size:10.0pt;line-height:107%;font-family:"Calibri",sans-serif;
mso-ascii-theme-font:minor-latin;mso-hansi-theme-font:
minor-latin;mso-bidi-theme-font:minor-latin;mso-ansi-language:EN-US;
;mso-bidi-language:AR-SA'><br clear=all style='page-break-before:always;
mso-break-type:section-break'>
</span></b>

<div class=WordSection4>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin;mso-no-proof:yes'><!--[if gte vml 1]><v:shape id="Picture_x0020_186"
 o:spid="_x0000_i1060" type="#_x0000_t75" style='width:275.4pt;height:211.8pt;
 visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image087.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=367 height=282
src="AstarSearch_Readme_images/image088.png" v:shapes="Picture_x0020_186"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_185" o:spid="_x0000_i1059" type="#_x0000_t75" style='width:280.8pt;
 height:3in;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image089.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=374 height=288
src="AstarSearch_Readme_images/image090.png" v:shapes="Picture_x0020_185"><![endif]></span><b
style='mso-bidi-font-weight:normal'><span style='font-size:10.0pt;line-height:
107%;mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin;mso-no-proof:yes'><!--[if gte vml 1]><v:shape
 id="Picture_x0020_87" o:spid="_x0000_i1058" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image091.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image092.png" v:shapes="Picture_x0020_87"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_88" o:spid="_x0000_i1057" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image093.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image094.png" v:shapes="Picture_x0020_88"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_89" o:spid="_x0000_i1056" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image095.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image096.png" v:shapes="Picture_x0020_89"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_90" o:spid="_x0000_i1055" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image097.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image098.png" v:shapes="Picture_x0020_90"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_91" o:spid="_x0000_i1054" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image099.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image100.png" v:shapes="Picture_x0020_91"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_92" o:spid="_x0000_i1053" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image023.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image101.png" v:shapes="Picture_x0020_92"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_93" o:spid="_x0000_i1052" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image025.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image102.png" v:shapes="Picture_x0020_93"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_94" o:spid="_x0000_i1051" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image103.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image104.png" v:shapes="Picture_x0020_94"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_95" o:spid="_x0000_i1050" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image105.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image106.png" v:shapes="Picture_x0020_95"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_96" o:spid="_x0000_i1049" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image107.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image108.png" v:shapes="Picture_x0020_96"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_97" o:spid="_x0000_i1048" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image033.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image109.png" v:shapes="Picture_x0020_97"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_98" o:spid="_x0000_i1047" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image110.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image111.png" v:shapes="Picture_x0020_98"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_99" o:spid="_x0000_i1046" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image112.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image113.png" v:shapes="Picture_x0020_99"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_100" o:spid="_x0000_i1045" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image114.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image115.png" v:shapes="Picture_x0020_100"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_101" o:spid="_x0000_i1044" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image041.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image116.png" v:shapes="Picture_x0020_101"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_102" o:spid="_x0000_i1043" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image117.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image118.png" v:shapes="Picture_x0020_102"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_103" o:spid="_x0000_i1042" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image119.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image120.png" v:shapes="Picture_x0020_103"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_104" o:spid="_x0000_i1041" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image121.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image122.png" v:shapes="Picture_x0020_104"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_105" o:spid="_x0000_i1040" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image049.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image123.png" v:shapes="Picture_x0020_105"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_106" o:spid="_x0000_i1039" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image124.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image125.png" v:shapes="Picture_x0020_106"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_107" o:spid="_x0000_i1038" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image126.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image127.png" v:shapes="Picture_x0020_107"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_108" o:spid="_x0000_i1037" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image128.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image129.png" v:shapes="Picture_x0020_108"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_109" o:spid="_x0000_i1036" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image057.png" o:title=""/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image130.png" v:shapes="Picture_x0020_109"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_110" o:spid="_x0000_i1035" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image131.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image132.png" v:shapes="Picture_x0020_110"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_111" o:spid="_x0000_i1034" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image133.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image134.png" v:shapes="Picture_x0020_111"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_112" o:spid="_x0000_i1033" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image135.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image136.png" v:shapes="Picture_x0020_112"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_113" o:spid="_x0000_i1032" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image065.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image137.png" v:shapes="Picture_x0020_113"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_114" o:spid="_x0000_i1031" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image138.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image139.png" v:shapes="Picture_x0020_114"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_115" o:spid="_x0000_i1030" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image140.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image141.png" v:shapes="Picture_x0020_115"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_116" o:spid="_x0000_i1029" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image071.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image142.png" v:shapes="Picture_x0020_116"><![endif]></span></b><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoNormal><b style='mso-bidi-font-weight:normal'><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;mso-no-proof:
yes'><!--[if gte vml 1]><v:shape id="Picture_x0020_117" o:spid="_x0000_i1028"
 type="#_x0000_t75" style='width:276.6pt;height:208.8pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image073.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image143.png" v:shapes="Picture_x0020_117"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_118" o:spid="_x0000_i1027" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image144.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image145.png" v:shapes="Picture_x0020_118"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_119" o:spid="_x0000_i1026" type="#_x0000_t75" style='width:276.6pt;
 height:208.8pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image146.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=369 height=278
src="AstarSearch_Readme_images/image147.png" v:shapes="Picture_x0020_119"><![endif]><!--[if gte vml 1]><v:shape
 id="Picture_x0020_120" o:spid="_x0000_i1025" type="#_x0000_t75" style='width:280.8pt;
 height:3in;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="AstarSearch_Readme_images/image148.png" o:title=""/>
 <o:lock v:ext="edit" aspectratio="f"/>
</v:shape><![endif]--><![if !vml]><img width=374 height=288
src="AstarSearch_Readme_images/image149.png" v:shapes="Picture_x0020_120"><![endif]></span></b><b><span
style='font-size:10.0pt;line-height:107%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal><b><span style='font-size:10.0pt;line-height:107%;
mso-bidi-font-family:Calibri;mso-bidi-theme-font:
minor-latin'><o:p>&nbsp;</o:p></span></b></p>

</div>

