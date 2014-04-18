% Title
% Daniel Wheeler
% 2014-04-27

# {#overview .step data-scale=8}

   
# {#title .step data-y=-1000}

<p class="title">Simulation and Data Management</p>

<p class="footer">
    Daniel Wheeler &bull;
    April 29, 2014 &bull;
    Diffusion Workshop
</p>


# {#automate .step data-y=200 data-x=-800}

# {#automate .step data-y=200 data-x=-800}

<br>
<p class="title"> Automate </p>

# About me {.step data-y=200 data-x=800}

<br>
scientific/academic code developer
<br>
<br>
run/manage simulations (code monkey)
<br>
<br>
an epic Pythonista (according to OSRC)
<br>
<br>
interested in reproducible research
<br>
<br>
see <code class="twitter">@wd15dan</code>

# Imagine... {.step data-y=200 data-x=2400}

<br>
A declarative metadata standard<p class="small"> that you can use to
tell a Linux VM how to download your data, execute your computational
analysis, and spin up an interface to a literate computing environment
with the analysis preloaded. Then we can provide buttons on scientific
papers that say "run this analysis on Rackspace! or Amazon! Estimated
cost: $25".</p>
<br>
Automated integration tests for papers <p class="small">
where you provide the metadata to run your analysis while you're
working on your paper and a service automatically pulls down your
analysis source and data, runs it, and generates your figures for you
to check. Then when the paper is ready to submit, the journal takes
your metadata format and verifies it themselves, and passes it on to
reviewers with a little "reproducible!" tick mark.
</p>
<br>
ideas by *C. Titus Brown*

# Orthogonal Issues {.step data-y=2500}

<div class="up-triangle"></div>

# Workflow Control {.step data-y=2710 data-x=180}

# Scientific Workflow {.step data-y=2300 data-x=240 data-scale=0.2}

<img class="center" src="images/workflow.png"></img>

# {#versioncontrol .step data-y=2710 data-x=-680 data-rotate-z="45"}


# Version Control {.step data-y=3110 data-x=-280 data-rotate-z="45"}

<br>
maintains history of workflow changes 
<br>
<br>
but not workflow usage
<br>
<br>
integrated into many scientific workflows

# Easy to use {.step data-y=3200 data-x=-500 data-rotate-z="45" data-scale=0.2}


~~~~{.console}
$ git init
$ git add file.txt
$ git ci -m "empty"
$ edit file.txt
$ git ci -am "hello"
$ git log
12e3c2618143 hello
e00433e69a43 empty
$ git push github master
~~~~

# Manage Complexity {.step data-y=3350 data-x=-350 data-rotate-z="-45" data-scale=0.2}

![](images/network.png)

# Event Control {.step data-rotate-z="-45" data-y=2700 data-x=560 }

provide a **unique ID (SHA checksum)** for every workflow execution
<br>
<br>
capture **meta-data**, not data
<br>
<br>
independent from **workflow control** and **version control**
<br>
<br>
partial solution: **Sumatra**, a simulation management tool (not workflow)




