% Title
% Daniel Wheeler
% 2014-04-27

# {#overview .step data-scale=8}

   
# {#title .step data-y=-2500 data-scale=4}

<p class="title">Simulation and Metadata Management</p>

<p class="footer">
    Daniel Wheeler &bull;
    September 23, 2014 &bull;
    MML Lab Visit
</p>


# {#automate .step data-y=200 data-x=-800}

# {#automate .step data-y=200 data-x=-800}

<br>
<p class="title"> Automate </p>

# Imagine... {.step .alwaysshow data-y=200 data-x=800}

<br>
A metadata standard for simulations<p class="small"> that
you can use to tell a Linux VM how to download your data, execute your
computational analysis </p>
<br>
Automated integration tests for papers <p class="small">
where you provide the metadata to run your analysis while you're
working on your paper and a service automatically pulls down your
analysis source/data and runs it
</p>



# Scientific Development Process {.step data-y=2000 data-x=500 data-scale=0.2}

<br>
<img class="center" src="images/workflow.png"></img>


# Orthogonal Issues {#orthogonal .step .alwaysshow data-y=2500}

<div class="up-triangle"></div>


# Workflow Control {.step .alwaysshow data-y=2720 data-x=180}


<!-- # {#versioncontrol .step .alwaysshow data-y=2910 data-x=-680 data-rotate-z="45"} -->

<!-- # {.step .alwaysshow data-y=2500} -->

# Version Control {.step .alwaysshow data-y=3110 data-x=-280 data-rotate-z="45"}

# {#vc .step data-y=3110 data-x=-280 data-rotate-z="45"}

<img class="vc" src="images/stack-of-files.png"></img>
<br>
maintains history of workflow changes 
<br>
<br>
but not workflow usage
<br>
<br>
already integrated into the scientific development process

# {.step .alwaysshow data-y=2500}  

# Event Control {.step .alwaysshow data-rotate-z="-45" data-y=2700 data-x=560 }

# {.step data-rotate-z="-45" data-y=2700 data-x=560 }

<br>
provide a **unique ID (SHA checksum)** for every workflow execution
<br>
<br>
capture **metadata**, not data
<br>
<br>
**not** workflow control or version control
<br>
<br>
partial solution: **Sumatra**, a simulation management tool (not workflow)

# {.step .alwaysshow data-y=2500}  

# Sumatra {.step data-x=-1000 data-y=1200 data-scale=0.5}

<br>
**doesn't change my workflow**
<br>
<br>
records the **metadata** (not the data): parameters, environment, data
location, time stamps, commit message, duration, data hash
<br>
<br>
generates **unique ID** for each simulation

# Sumatra Records {#webinterface .step data-x=800 data-y=1200 data-scale=0.5}

<iframe width="100%" height="100%" src="http://127.0.0.1:8000/" frameborder="0" border="0"> </iframe>

# Using IPython {#webinterface2 .step data-x=3800 data-y=1200 data-scale=0.5}

<iframe width="100%" height="100%" src="http://wd15.github.io/2013/05/07/extremefill2d/" frameborder="0" border="0"> </iframe>

# {.step data-y=200 data-x=800}

# The Fantasy {.step data-x=3400 data-y=200 data-scale=0.5}

<br>
cloud service for Sumatra
<br>
<br>
integrated with Github, Buildbot and a VM provider
<br>
<br>
**Yannick Congo** (guest researcher) will start soon!

# Thanks! {.step data-x=4400 data-y=200 data-scale=0.5}

<br>
slides: [wd15.github.io/diffusion-workshop-2014](http://wd15.github.io/diffusion-workshop-2014/)
<br>
<br>
parallel demo: [github.com/wd15/smt-demo](https://github.com/wd15/smt-demo)
