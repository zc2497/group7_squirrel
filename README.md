<table>
<h1>group7_squirrel
</h1>
<br>
<h2>Project description
</h2>
<p>We built a web application to keep track of all squirrels of Central Park. Users are allowed to add, update and view squirrel data.</p>
<p>We import 2018 Central Park Squirrel Census data from <a href='https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'>here</a> as squirreldata.csv file. We also export the squirrel data as export.csv file in our github repository. After making some changes, if you want to export again, you can run this command "python manage.py export<u>_</u>squirrel<u>_</u>data export.csv". In addition, you can also import this export.csv file again.</p>
<br>
<h3>Detail description</h3>
<br>
<p>At the main page"/sightings",there is a link to add new squirrels, a link to show the map of the first 100 squirrels, and a link to show some stats about the squirrels. Below these links, the unique IDs of all squirrels in our dataset is shown in a list,a link to see details, delete or update has been attached to each squirrel.
</p>
<br>
<p>Add page"/sightings/add",you can add a new squirrel,after you add successfully, it will redirect you to the main page; if you don't want to add anymore, there is a link next to submit button for you to go directly back to main page. 
</p>
<br>
<p>Map page"/map",you can see the markers  of the first 100 suirrels at Central Park.
</p>
<br>
<p>Stats page"/sightings/stats", you can see some stats about the squirrels with the attributes we chose.
</p>
<br>
<p>Update page"/sightings/&lt;unique-squirrel-id&gt;/update", you can update any information about this particular squirrel, and when you update successfully, you will be redirected to this squirrel's detail page; if you don't want to update anymore, there is a link next to submit
 button for you to go directly back to main page. 
</p>
<br>
<p>Delete page"/sightings/&lt;unique-squirrel-id&gt;/delete", if you are sure you want to delete this squirrel, you can delete it here, after you delete successfully, you will be redirected to the main page, if you don't want to update anymore, there is a link next to delete button for you to go directly back to main page.
</p>
<br>
<h2>Group name and section: Project Group 7, Section 2
</h2>
<br>
<h2>UNIs: [zc2497, rj2578]
</h2>
<br>
<h2>The link to the server running our application:<a href='https://instance1-255500.appspot.com/'>https://instance1-255500.appspot.com/</a>
</h2>
</table>
