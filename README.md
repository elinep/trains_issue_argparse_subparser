# summary
minimal example to demonstrate issues with trains and subparser.

**script.py** expects global arguments and sub-commands argument.
The default value for each argument is **1**. We will try to set 
all parameters to **2** using the commandline and using the remote
 execution thanks to **trains-agent**.
 
# procedure
## venv
Let's create the venv.
```
# create venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## run task locally
run main task and override defaults parameters

```
python script.py --global_param0 2 --global_param1 2 program --specific_param0 2 --specific_param1 2
```

Which outputs: 
```
TRAINS Task: overwriting (reusing) task id=7270c5a3905e4186acc08f9b499749ca
TRAINS results page: https://demoapp.trains.allegro.ai/projects/5536614fa22443e1a01113cc38eedf81/experiments/7270c5a3905e4186acc08f9b499749ca/output/log
parsed arguments:
Namespace(global_param0=2, global_param1='2', specific_param0=2, specific_param1='2', sub_program='program')
```

## run task remotely
now we use train agent to run the same task remotely. We use the task id created above.
```
trains-agent execute --id 7270c5a3905e4186acc08f9b499749ca
```
and the associated output:
```
Current configuration (trains_agent v0.12.2, location: /home/peline/trains.conf):
----------------------
sdk.storage.cache.default_base_dir = ~/.trains/cache
sdk.storage.cache.size.min_free_bytes = 10GB
sdk.storage.direct_access.0.url = file://*
sdk.metrics.file_history_size = 100
sdk.metrics.matplotlib_untitled_history_size = 100
sdk.metrics.images.format = JPEG
sdk.metrics.images.quality = 87
sdk.metrics.images.subsampling = 0
sdk.network.metrics.file_upload_threads = 4
sdk.network.metrics.file_upload_starvation_warning_sec = 120
sdk.network.iteration.max_retries_on_server_error = 5
sdk.network.iteration.retry_backoff_factor_sec = 10
sdk.aws.s3.key = 
sdk.aws.s3.region = 
sdk.aws.boto3.pool_connections = 512
sdk.aws.boto3.max_multipart_concurrency = 16
sdk.log.null_log_propagate = false
sdk.log.task_log_buffer_capacity = 66
sdk.log.disable_urllib3_info = true
sdk.development.task_reuse_time_window_in_hours = 72.0
sdk.development.vcs_repo_detect_async = true
sdk.development.store_uncommitted_code_diff_on_train = true
sdk.development.support_stopping = true
sdk.development.worker.report_period_sec = 2
sdk.development.worker.ping_period_sec = 30
sdk.development.worker.log_stdout = true
logging.version = 1
logging.loggers.urllib3.level = ERROR
agent.worker_id = 
agent.worker_name = peline-HP-Compaq-8100-Elite-SFF-PC
agent.python_binary = 
agent.package_manager.type = pip
agent.package_manager.system_site_packages = false
agent.package_manager.force_upgrade = false
agent.package_manager.conda_channels.0 = defaults
agent.package_manager.conda_channels.1 = conda-forge
agent.package_manager.conda_channels.2 = pytorch
agent.venvs_dir = /home/peline/.trains/venvs-builds
agent.vcs_cache.enabled = true
agent.vcs_cache.path = /home/peline/.trains/vcs-cache
agent.venv_update.enabled = false
agent.pip_download_cache.enabled = true
agent.pip_download_cache.path = /home/peline/.trains/pip-download-cache
agent.translate_ssh = true
agent.reload_config = false
agent.docker_pip_cache = /home/peline/.trains/pip-cache
agent.docker_apt_cache = /home/peline/.trains/apt-cache
agent.default_docker.image = nvidia/cuda
agent.default_python = 3.7
agent.cuda_version = 0
agent.cudnn_version = 0
api.version = 1.5
api.verify_certificate = true
api.default_version = 1.5
api.http.max_req_size = 15728640
api.http.retries.total = 240
api.http.retries.connect = 240
api.http.retries.read = 240
api.http.retries.redirect = 240
api.http.retries.status = 240
api.http.retries.backoff_factor = 1.0
api.http.retries.backoff_max = 120.0
api.http.wait_on_maintenance_forever = true
api.http.pool_maxsize = 512
api.http.pool_connections = 512

Executing task id [7270c5a3905e4186acc08f9b499749ca]:
repository = https://github.com/elinep/trains_issue_argparse_subparser.git
branch = master
version_num = 33f811afca38b67d5085a1df986cb7e2a76678b5
tag = 
entry_point = script.py
working_dir = .

Using base prefix '/usr'
New python executable in /home/peline/.trains/venvs-builds/3.7/bin/python3.7
Also creating executable in /home/peline/.trains/venvs-builds/3.7/bin/python
Installing setuptools, pip, wheel...
done.


Using cached repository in "/home/peline/.trains/vcs-cache/trains_issue_argparse_subparser.git.5145cf108810cff38af064ff3008638d/trains_issue_argparse_subparser.git"
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 5 (delta 1), reused 5 (delta 1), pack-reused 0
Dépaquetage des objets: 100% (5/5), fait.
Depuis https://github.com/elinep/trains_issue_argparse_subparser
   7f3dc2f..33f811a  master     -> origin/master
Note : extraction de '33f811afca38b67d5085a1df986cb7e2a76678b5'.

Vous êtes dans l'état « HEAD détachée ». Vous pouvez visiter, faire des modifications
expérimentales et les valider. Il vous suffit de faire une autre extraction pour
abandonner les commits que vous faites dans cet état sans impacter les autres branches

Si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
il vous suffit d'utiliser « checkout -b » (maintenant ou plus tard) comme ceci :

  git checkout -b <nom-de-la-nouvelle-branche>

HEAD est maintenant sur 33f811a initial commit
type: git
url: https://github.com/elinep/trains_issue_argparse_subparser.git
branch: HEAD
commit: 33f811afca38b67d5085a1df986cb7e2a76678b5
root: /home/peline/.trains/venvs-builds/3.7/task_repository/trains_issue_argparse_subparser.git


Requirement already up-to-date: pip in /home/peline/.trains/venvs-builds/3.7/lib/python3.7/site-packages (19.3.1)
Collecting Cython
  Using cached https://files.pythonhosted.org/packages/d8/58/2deb24de3c10cc4c0f09639b46f4f4b50059f0fdc785128a57dd9fdce026/Cython-0.29.14-cp37-cp37m-manylinux1_x86_64.whl
Installing collected packages: Cython
Successfully installed Cython-0.29.14
Collecting trains
  Using cached https://files.pythonhosted.org/packages/6e/40/b625bc6ac9196ad7b73d67e5ac5238f87e6a6e6cc84b36587d8058472a49/trains-0.12.2-py2.py3-none-any.whl
Collecting tqdm>=4.19.5
  Using cached https://files.pythonhosted.org/packages/72/c9/7fc20feac72e79032a7c8138fd0d395dc6d8812b5b9edf53c3afd0b31017/tqdm-4.41.1-py2.py3-none-any.whl
Collecting pyjwt>=1.6.4
  Using cached https://files.pythonhosted.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl
Processing /home/peline/.cache/pip/wheels/52/41/b0/bf50409fe2b1d3b79afa3eed71b54b3e30fe5b695db2c7ba2e/psutil-5.6.7-cp37-cp37m-linux_x86_64.whl
Collecting urllib3>=1.21.1
  Using cached https://files.pythonhosted.org/packages/b4/40/a9837291310ee1ccc242ceb6ebfd9eb21539649f193a7c8c86ba15b98539/urllib3-1.25.7-py2.py3-none-any.whl
Collecting pyparsing>=2.0.3
  Using cached https://files.pythonhosted.org/packages/5d/bc/1e58593167fade7b544bfe9502a26dc860940a79ab306e651e7f13be68c2/pyparsing-2.4.6-py2.py3-none-any.whl
Collecting plotly>=3.9.0
  Using cached https://files.pythonhosted.org/packages/8e/ce/6ea5683c47b682bffad39ad41d10913141b560b1b875a90dbc6abe3f4fa9/plotly-4.4.1-py2.py3-none-any.whl
Processing /home/peline/.cache/pip/wheels/54/b7/c7/2ada654ee54483c9329871665aaf4a6056c3ce36f29cf66e67/PyYAML-5.2-cp37-cp37m-linux_x86_64.whl
Collecting funcsigs>=1.0
  Using cached https://files.pythonhosted.org/packages/69/cb/f5be453359271714c01b9bd06126eaf2e368f1fddfff30818754b5ac2328/funcsigs-1.0.2-py2.py3-none-any.whl
Collecting requests-file>=1.4.2
  Using cached https://files.pythonhosted.org/packages/23/9c/6e63c23c39e53d3df41c77a3d05a49a42c4e1383a6d2a5e3233161b89dbf/requests_file-1.4.3-py2.py3-none-any.whl
Collecting humanfriendly>=2.1
  Using cached https://files.pythonhosted.org/packages/90/df/88bff450f333114680698dc4aac7506ff7cab164b794461906de31998665/humanfriendly-4.18-py2.py3-none-any.whl
Collecting typing>=3.6.4
  Using cached https://files.pythonhosted.org/packages/fe/2e/b480ee1b75e6d17d2993738670e75c1feeb9ff7f64452153cf018051cc92/typing-3.7.4.1-py3-none-any.whl
Collecting six>=1.11.0
  Using cached https://files.pythonhosted.org/packages/65/26/32b8464df2a97e6dd1b656ed26b2c194606c16fe163c695a992b36c11cdf/six-1.13.0-py2.py3-none-any.whl
Collecting jsonschema>=2.6.0
  Using cached https://files.pythonhosted.org/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl
Collecting requests>=2.20.0
  Using cached https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl
Collecting jsonmodels>=2.2
  Using cached https://files.pythonhosted.org/packages/e9/c4/93ce38601474210eeb97b50c7f65d48827ee19f5e7b6e51b63b3684059df/jsonmodels-2.4-py2.py3-none-any.whl
Collecting furl>=2.0.0
  Using cached https://files.pythonhosted.org/packages/9f/c7/e9dc30914bf048bcd06284bb93d9650d318ecac8668b684fc41e975558ff/furl-2.1.0-py2.py3-none-any.whl
Collecting Pillow>=4.1.1
  Using cached https://files.pythonhosted.org/packages/f5/79/b2d5695d1a931474fa68b68ec93bdf08ba9acbc4d6b3b628eb6aac81d11c/Pillow-7.0.0-cp37-cp37m-manylinux1_x86_64.whl
Collecting pathlib2>=2.3.0
  Using cached https://files.pythonhosted.org/packages/e9/45/9c82d3666af4ef9f221cbb954e1d77ddbb513faf552aea6df5f37f1a4859/pathlib2-2.3.5-py2.py3-none-any.whl
Collecting pigar==0.9.2
  Using cached https://files.pythonhosted.org/packages/68/12/705a7aa3fae1012338a35c07c7b27afc23c44ba3bd3c3d50dac982d729e7/pigar-0.9.2-py2.py3-none-any.whl
Collecting attrs>=18.0
  Using cached https://files.pythonhosted.org/packages/a2/db/4313ab3be961f7a763066401fb77f7748373b6094076ae2bda2806988af6/attrs-19.3.0-py2.py3-none-any.whl
Collecting numpy>=1.10
  Using cached https://files.pythonhosted.org/packages/20/53/127cb49435bcf5d841baf8eafa030931c62a9eac577a641f8c2293d23371/numpy-1.18.0-cp37-cp37m-manylinux1_x86_64.whl
Processing /home/peline/.cache/pip/wheels/8b/99/a0/81daf51dcd359a9377b110a8a886b3895921802d2fc1b2397e/future-0.18.2-cp37-none-any.whl
Collecting python-dateutil>=2.6.1
  Using cached https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl
Processing /home/peline/.cache/pip/wheels/d7/a9/33/acc7b709e2a35caa7d4cae442f6fe6fbf2c43f80823d46460c/retrying-1.3.3-cp37-none-any.whl
Collecting importlib-metadata; python_version < "3.8"
  Using cached https://files.pythonhosted.org/packages/e9/71/1a1e0ed0981bb6a67bce55a210f168126b7ebd2065958673797ea66489ca/importlib_metadata-1.3.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in /home/peline/.trains/venvs-builds/3.7/lib/python3.7/site-packages (from jsonschema>=2.6.0->trains->-r /tmp/cached-reqsowtoxau0.txt (line 1)) (44.0.0)
Processing /home/peline/.cache/pip/wheels/83/89/d3/1712b9c33c9b9c0911b188a86aeff2a9a05e113f986cf79d92/pyrsistent-0.15.6-cp37-cp37m-linux_x86_64.whl
Collecting chardet<3.1.0,>=3.0.2
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting certifi>=2017.4.17
  Using cached https://files.pythonhosted.org/packages/b9/63/df50cac98ea0d5b006c55a399c3bf1db9da7b5a24de7890bc9cfd5dd9e99/certifi-2019.11.28-py2.py3-none-any.whl
Collecting idna<2.9,>=2.5
  Using cached https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl
Collecting orderedmultidict>=1.0.1
  Using cached https://files.pythonhosted.org/packages/04/16/5e95c70bda8fe6ea715005c0db8e602400bdba50ae3c72cb380eba551289/orderedmultidict-1.0.1-py2.py3-none-any.whl
Collecting colorama>=0.3.9
  Using cached https://files.pythonhosted.org/packages/c9/dc/45cdef1b4d119eb96316b3117e6d5708a08029992b2fee2c143c7a0a5cc5/colorama-0.4.3-py2.py3-none-any.whl
Collecting zipp>=0.5
  Using cached https://files.pythonhosted.org/packages/74/3d/1ee25a26411ba0401b43c6376d2316a71addcc72ef8690b101b4ea56d76a/zipp-0.6.0-py2.py3-none-any.whl
Collecting more-itertools
  Using cached https://files.pythonhosted.org/packages/68/03/0604cec1ea13c9f063dd50f900d1a36160334dd3cfb01fd0e638f61b46ba/more_itertools-8.0.2-py3-none-any.whl
Installing collected packages: tqdm, pyjwt, psutil, urllib3, pyparsing, six, retrying, plotly, PyYAML, funcsigs, chardet, certifi, idna, requests, requests-file, humanfriendly, typing, more-itertools, zipp, importlib-metadata, pyrsistent, attrs, jsonschema, python-dateutil, jsonmodels, orderedmultidict, furl, Pillow, pathlib2, colorama, pigar, numpy, future, trains
Successfully installed Pillow-7.0.0 PyYAML-5.2 attrs-19.3.0 certifi-2019.11.28 chardet-3.0.4 colorama-0.4.3 funcsigs-1.0.2 furl-2.1.0 future-0.18.2 humanfriendly-4.18 idna-2.8 importlib-metadata-1.3.0 jsonmodels-2.4 jsonschema-3.2.0 more-itertools-8.0.2 numpy-1.18.0 orderedmultidict-1.0.1 pathlib2-2.3.5 pigar-0.9.2 plotly-4.4.1 psutil-5.6.7 pyjwt-1.7.1 pyparsing-2.4.6 pyrsistent-0.15.6 python-dateutil-2.8.1 requests-2.22.0 requests-file-1.4.3 retrying-1.3.3 six-1.13.0 tqdm-4.41.1 trains-0.12.2 typing-3.7.4.1 urllib3-1.25.7 zipp-0.6.0
Running task id [7270c5a3905e4186acc08f9b499749ca]:
[.]$ /home/peline/.trains/venvs-builds/3.7/bin/python -u script.py
Summary - installed python packages:
pip:
- attrs==19.3.0
- certifi==2019.11.28
- chardet==3.0.4
- colorama==0.4.3
- Cython==0.29.14
- funcsigs==1.0.2
- furl==2.1.0
- future==0.18.2
- humanfriendly==4.18
- idna==2.8
- importlib-metadata==1.3.0
- jsonmodels==2.4
- jsonschema==3.2.0
- more-itertools==8.0.2
- numpy==1.18.0
- orderedmultidict==1.0.1
- pathlib2==2.3.5
- pigar==0.9.2
- Pillow==7.0.0
- plotly==4.4.1
- psutil==5.6.7
- PyJWT==1.7.1
- pyparsing==2.4.6
- pyrsistent==0.15.6
- python-dateutil==2.8.1
- PyYAML==5.2
- requests==2.22.0
- requests-file==1.4.3
- retrying==1.3.3
- six==1.13.0
- tqdm==4.41.1
- trains==0.12.2
- typing==3.7.4.1
- urllib3==1.25.7
- zipp==0.6.0

Environment setup completed successfully

Starting Task Execution:

Storing stdout and stderr log into [/tmp/.trains_agent_out.j6bp7vz3.txt]
TRAINS results page: https://demoapp.trains.allegro.ai/projects/5536614fa22443e1a01113cc38eedf81/experiments/7270c5a3905e4186acc08f9b499749ca/output/log
parsed arguments:
Namespace(global_param0=2, global_param1=2.0, specific_param1=2.0, sub_program='program')


Leaving process id 15421
```

## explanation
Next table summarize the result and the expected behavior

| params          | expected  | local run | remote run |
|-----------------|:---------:|:---------:|:----------:|
| global_param0   |     2     |     2     |      2     |
| global_param1   |    '2'    |    '2'    |     2.0    |
| sub_program     | 'program' | 'program' |  'program' |
| specific_param0 |     2     |     2     |            |
| specific_param1 |    '2'    |    '2'    |     2.0    |
 
There are 2 issues:
- (minor) when type is not set the remote run doesn't not behave like 
argparse ('global_param1' and 'specific_param1').
- for remote execution, sub parser arguments are not set when type is set to int.
