Search.setIndex({docnames:["api/data_sources","api/element","api/elements","api/field","api/fieldscontainer","api/index","api/meshed_region","api/model","api/operator","api/plotting","api/wrapped_operators","contributing","examples/00-basic/00-basic_example","examples/00-basic/01-basic_operators","examples/00-basic/02-basic_field_containers","examples/00-basic/sg_execution_times","examples/01-static-transient/00-basic_transient","examples/01-static-transient/sg_execution_times","examples/index","getting_started/docker","getting_started/index","getting_started/install","index","user_guide/index","user_guide/model"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.todo":2,sphinx:56},filenames:["api/data_sources.rst","api/element.rst","api/elements.rst","api/field.rst","api/fieldscontainer.rst","api/index.rst","api/meshed_region.rst","api/model.rst","api/operator.rst","api/plotting.rst","api/wrapped_operators.rst","contributing.rst","examples/00-basic/00-basic_example.rst","examples/00-basic/01-basic_operators.rst","examples/00-basic/02-basic_field_containers.rst","examples/00-basic/sg_execution_times.rst","examples/01-static-transient/00-basic_transient.rst","examples/01-static-transient/sg_execution_times.rst","examples/index.rst","getting_started/docker.rst","getting_started/index.rst","getting_started/install.rst","index.rst","user_guide/index.rst","user_guide/model.rst"],objects:{"ansys.dpf.core":{operators_helper:[10,2,0,"-"]},"ansys.dpf.core.data_sources":{DataSources:[0,0,1,""]},"ansys.dpf.core.data_sources.DataSources":{_connect:[0,1,1,""],add_file_path:[0,1,1,""],add_upstream:[0,1,1,""],set_result_file_path:[0,1,1,""]},"ansys.dpf.core.dpf_operator":{Operator:[8,0,1,""]},"ansys.dpf.core.dpf_operator.Operator":{connect:[8,1,1,""],get_output:[8,1,1,""],run:[8,1,1,""]},"ansys.dpf.core.field":{Field:[3,0,1,""]},"ansys.dpf.core.field.Field":{component_count:[3,1,1,""],data:[3,1,1,""],elementary_data_count:[3,1,1,""],elementary_data_shape:[3,1,1,""],get_entity_data:[3,1,1,""],get_entity_data_by_id:[3,1,1,""],location:[3,1,1,""],max:[3,1,1,""],min:[3,1,1,""],plot:[3,1,1,""],resize:[3,1,1,""],scoping:[3,1,1,""],set_entity_data:[3,1,1,""],shape:[3,1,1,""],shell_layers:[3,1,1,""],size:[3,1,1,""],unit:[3,1,1,""]},"ansys.dpf.core.fields_container":{FieldsContainer:[4,0,1,""]},"ansys.dpf.core.fields_container.FieldsContainer":{add_field:[4,1,1,""],get_fields:[4,1,1,""],get_fields_by_time_complex_ids:[4,1,1,""],select_component:[4,1,1,""]},"ansys.dpf.core.meshed_region":{Element:[1,0,1,""],Elements:[2,0,1,""]},"ansys.dpf.core.meshed_region.Element":{id:[1,1,1,""],index:[1,1,1,""],n_nodes:[1,1,1,""],node_ids:[1,1,1,""],nodes:[1,1,1,""],shape:[1,1,1,""],type:[1,1,1,""]},"ansys.dpf.core.meshed_region.Elements":{connectivities_field:[2,1,1,""],element_by_id:[2,1,1,""],element_by_index:[2,1,1,""],element_types_field:[2,1,1,""],map_scoping:[2,1,1,""],mapping_id_to_index:[2,1,1,""],materials_field:[2,1,1,""],n_elements:[2,1,1,""],scoping:[2,1,1,""]},"ansys.dpf.core.model":{Model:[7,0,1,""]},"ansys.dpf.core.model.Model":{metadata:[24,1,1,""],operator:[7,1,1,""],plot:[7,1,1,""],results:[24,1,1,""]},"ansys.dpf.core.operators_helper":{add:[10,3,1,""],build_docs:[10,3,1,""],component_selector:[10,3,1,""],dot_tensor:[10,3,1,""],element_dot:[10,3,1,""],eqv:[10,3,1,""],min_max:[10,3,1,""],norm:[10,3,1,""],sqr:[10,3,1,""],sum:[10,3,1,""],to_nodal:[10,3,1,""]},"ansys.dpf.core.plotter":{Plotter:[9,2,0,"-"]}},objnames:{"0":["py","class","Python class"],"1":["py","method","Python method"],"2":["py","module","Python module"],"3":["py","function","Python function"]},objtypes:{"0":"py:class","1":"py:method","2":"py:module","3":"py:function"},terms:{"00000":16,"00000000e":[3,14],"00062674":16,"00218":16,"0025094":16,"00564185":16,"00709302e":3,"00798431":16,"00891":16,"00952":16,"00999992":16,"01173895e":14,"01201879":16,"01244994":16,"01251":16,"01364486e":14,"01378":16,"0137951":16,"01403":16,"01552154":16,"01743770e":14,"01787116":16,"01791331e":3,"019975":16,"02121":16,"02207871":16,"02310":16,"02681396e":12,"02704768e":14,"02759782":16,"02944459":16,"03000":16,"03186142e":3,"03413897e":14,"03478255":16,"03526532":16,"03725894":16,"03733769":16,"039975":16,"04062977":16,"0418829":16,"04272116":16,"04310436":16,"04499722":16,"04515762e":3,"05130461":16,"05195353":16,"05358419":16,"05703912":16,"05715204":16,"05897617":16,"05913066":16,"05919802e":14,"05942392":16,"05950852":16,"05982844":16,"059975":16,"06042056":16,"06077103":16,"06212713e":14,"07400000e":14,"07537743e":14,"079975":16,"08050063e":14,"087e":6,"08989140e":14,"09077164e":14,"09503532e":3,"099975":16,"0x7f9a5d150b40":6,"0x7f9a64b41910":6,"101":[13,15],"102":[14,15],"10540890e":14,"11190":6,"11284":2,"11286":2,"11287":2,"119975":16,"127":19,"139975":16,"14214033e":14,"14726184e":14,"159975":16,"16046741e":14,"16452955e":14,"179":6,"179975":16,"18477336e":14,"186":[12,15],"19096032e":14,"19379712e":12,"19494216e":12,"199975":16,"1mbool_rotate_to_glob":13,"1mdata_sourc":13,"1mdomain_id":13,"1mfields_contain":13,"1mmesh":13,"1mmesh_scop":13,"1mrequested_loc":13,"1mstreams_contain":13,"1mtime_scop":13,"20201r1":20,"2021r1":[11,12,20,21],"20291800e":14,"20861254e":12,"209":[16,17],"21536180e":3,"218975":16,"219":16,"22188426e":12,"22753781e":12,"23026491e":14,"238975":16,"239":16,"2400404500674":1,"24684037e":14,"24982":[2,6],"25103522e":14,"25762828e":14,"25860708e":14,"258975":16,"259":16,"26430754e":14,"26474":2,"26656":2,"268e":6,"27090":2,"2732":2,"2734":2,"2736":2,"273e":6,"27831232e":12,"278975":16,"279":16,"28246347e":3,"28563":2,"28617350e":14,"28782940e":12,"28947":2,"29101":2,"29246409e":12,"29356739e":14,"29502":[1,2],"29503":2,"297e":6,"298975":16,"299":16,"299e":6,"3000":12,"318975":16,"319":16,"31904602e":14,"32988359e":14,"329e":6,"33058082e":14,"331e":6,"33676924e":14,"338975":16,"339":16,"34398104e":14,"35051199e":14,"358975":16,"359":16,"35911608e":12,"3751":12,"378975":16,"379":16,"3820":[3,16,24],"388":15,"39214534e":3,"398975":16,"399":16,"417975":16,"418":16,"42766633e":14,"43440783e":14,"43688328e":14,"437975":16,"438":16,"44002311e":14,"44669483e":14,"44722939e":14,"457975":16,"458":16,"46666013e":12,"477975":16,"478":16,"4815370582001863e":13,"48153706e":13,"495e":6,"497975":16,"498":16,"50054":[11,19],"50544246e":14,"508":16,"509":16,"513":16,"51723816e":3,"517975":16,"518":16,"523":2,"524":16,"52485289e":12,"525":16,"52559428e":12,"52577102e":12,"52834607e":14,"531":2,"532":2,"533":16,"534":16,"53485079e":14,"53720678e":14,"53754972":16,"538":16,"54190337e":14,"55180700e":14,"557":16,"55725277":16,"55960665e":14,"5720":3,"577":16,"57711786":16,"59176333e":3,"59300974e":14,"597":16,"59702054":16,"61320844e":14,"61694639":16,"617":16,"63117832e":12,"63247":1,"63631":1,"63683347":16,"637":16,"64096553e":14,"64249826e":12,"65561":6,"65673452":16,"657":16,"66039":2,"66448574e":14,"67662783":16,"676628":3,"677":16,"69632909e":12,"700e":6,"703e":6,"71912713e":14,"71987":6,"72144":6,"72145":6,"72150":6,"72324787407068":1,"73823999e":14,"759":[7,24],"760":[7,24],"76060480e":3,"761":[7,24],"763":[7,24],"77906905e":14,"789":16,"80845567299105":1,"81104389e":14,"8855":6,"89019831e":14,"89155604e":14,"89858785e":14,"908":16,"909":16,"910":16,"91212290e":12,"91446544e":14,"92077883e":14,"92690969e":14,"93565975e":14,"case":[8,11,13],"class":[5,11,12,13,19],"default":[0,3,6,7,8,11,12,13,16,19],"enum":[3,6],"export":[11,19],"final":[11,12,13],"function":[5,10,11,13],"import":[0,1,2,3,6,7,8,10,11,12,13,14,16,19,22,24],"int":[1,2,3,4,8,10,13],"new":[10,22],"null":13,"public":[5,11],"return":[1,2,3,4,6,7,10,12,13,14,16,24],"short":19,"static":[3,7,12,13,14,16,17,18,22,24],"transient":[3,17],"true":[6,7,13,16],"while":[11,14],And:19,For:[3,8,11,12,14,16,20,24],IDs:[1,6,14,16],NOT:11,PRs:11,That:[2,6],The:[2,3,4,7,8,10,11,12,13,14,16,22,23],Then:[11,16],There:[11,19],These:[2,10,11,18],Useful:[2,6],Using:[10,14,20],With:[12,13,14,16],__version__:11,_connect:0,_version:11,about:[11,14],abov:11,absolut:[11,24],accept:7,access:[6,7,12,19,22,24],accord:19,accumul:7,acknowledg:11,across:11,act:22,action:11,activ:11,add:[0,4,10,11],add_field:4,add_file_path:0,add_upstream:0,added:[3,11,22],addit:[6,11],addition:[11,16],address:11,advantag:[19,22],after:11,agnost:22,alexand:11,all:[1,2,6,10,11,12,13,14,21],allclos:16,alloc:[3,13],allow:[7,11,13,22],alreadi:13,also:[0,11,12,14,22],alwai:[11,14,19],amount:22,ampl:11,analysi:[4,7,12,13,14,17,22,24],analysis_typ:24,ani:[11,14,19],ansi:[0,1,2,3,4,6,7,8,10,11,12,13,14,16,18,19,20,21,22,24],api:11,appli:14,applic:[11,19],approach:[11,13],appropri:[7,11,24],approv:11,architectur:22,argument:6,around:22,arr_a:10,arr_b:10,arrai:[2,3,6,10,12,14,16],asarrai:10,ask:[8,11],assembl:14,associ:[2,6,7,14],assum:19,attempt:[4,11,12,19],attribut:24,author:[11,19],autodoc:11,autom:[6,11],automat:[11,12,13],avail:[7,10,11,12,13,14,16,22,24],averag:10,avoid:19,axes:6,axi:14,azur:11,background:[11,12],base:[1,2,3,7,11,14,16,22,24],basic:[11,15,23,24],basic_exampl:[12,15],basic_field_contain:[14,15],basic_oper:[13,15],basic_transi:[16,17],bat:11,beam:1,been:22,befor:[11,14],begin:16,behavior:[18,19],belong:[1,2,4,6],below:11,best:11,between:[2,10,14],bfe:[7,24],binari:19,bool:[3,6],both:11,bound:6,broken:11,browser:11,bugfix:11,build:10,build_doc:10,built:[10,11],cach:11,call:22,can:[0,1,2,3,4,7,8,11,12,13,14,16,19,21,22,24],candid:11,capabl:22,captur:[0,2,8],care:12,cat:19,caught:11,cell:6,cento:20,certain:[14,24],chain:[10,13,16,22],chanc:11,chang:11,channel:[0,3,4,6,7,8],check:11,clean:11,click:[12,13,14,16],client:14,clone:21,close:11,cluster:19,co_energi:[7,12,13,14,16,22,24],code:[12,13,14,16],collect:[2,6,11,14],color:7,com:[11,19,20,21],command:19,commerci:11,commit:11,common:3,commun:11,compar:[11,13],compat:11,compil:11,complet:14,complex:[4,11,12,13,14,16,22],complexid:4,compliant:11,compon:[3,4,10,14,16],component:22,component_count:3,component_selector:10,comput:[7,10,11,16,22,24],concept:18,conduct:11,connect:[0,2,3,4,7,8,11,12,13,14,16,19,24],connect_to_serv:[12,19],connectivities_field:2,consid:11,consist:19,contain:[1,3,4,6,10,11,12,13,15,16,18,24],container:[19,20],continu:22,contribut:21,contributor:11,conveienc:14,conveni:[3,13],coordin:[1,13,24],coordinates_field:[16,24],copi:20,core:[0,1,2,3,4,5,6,7,8,9,10,13,14,15,16,18,19,21,24],correct:11,correspond:[1,4,6],cov:11,coverag:11,crash:11,creat:[0,1,4,7,8,12,13,14,16,19,24],creation:10,credenti:19,critic:11,csv:22,cumul:[12,13,14,16],current:[10,11,19],custom:22,dat:0,data:[2,3,5,7,10,11,12,13,16,22,24],data_sourc:[0,7,12,13,24],data_sources_pb2:0,datas:3,datasetattribut:6,datasourc:[0,7,8,13],deem:11,defin:[14,22],delet:11,demo:18,demonstr:[13,18],depend:11,dependaci:21,deploi:11,deploy:[11,19],describ:[14,22],descript:[7,11,24],design:22,detail:[11,20,22],develop:22,dict:4,did:11,differ:[4,11,16],dimensionn:14,directli:[0,3,6,11,13,14,19,24],directori:[10,11,19],discuss:11,disp:[3,6,7,12,16],disp_field:4,disp_op:[8,13,14],disp_x_field:4,disp_z:16,displac:[3,6,7,14,18,22,24],displacement_0:3,displacement_1:[13,14],displai:[12,16,24],doc:11,docker:[11,20],docstr:11,document:10,doe:14,don:11,dot:10,dot_tensor:10,doubl:[3,8,14],doubt:11,down:11,download:[12,13,14,16,19,21],download_transient_result:[3,16],dpf:[0,1,2,3,4,5,6,7,8,9,10,13,14,15,16,20,21,23],dpf_core:[12,19],dpf_ip:[11,19],dpf_oper:8,dpf_port:[11,19],dpf_start_serv:[11,19],dtype:2,due:21,dure:11,dynam:[3,11],e_vol:10,each:[2,3,4,10,11,13,14,16,22],eas:19,easi:[12,22],easier:13,easili:[13,22],echo:19,ecosystem:20,edot:10,effect:11,effici:[3,13,22],effort:11,either:[0,3,7,10,12],element:[3,5,6,7,10,12,13,14,16,24],element_by_id:2,element_by_index:2,element_dot:10,element_nodal_forc:[7,12,16,22,24],element_types_field:2,element_volum:10,elementalnod:[3,7,24],elementari:[3,8,10,14],elementary_data_count:3,elementary_data_shap:3,elementid:1,els:11,enabl:[6,11,22],encapsul:7,encount:11,encourag:11,end:10,energy_stiffness_matrix:[7,12,13,14,16,22,24],engin:22,ensur:11,entir:[14,16],entiti:[2,3,6,13,14,22],entri:16,environ:[11,19,22],equival:[2,10,14,16],eqv:[10,16],eqv_max:16,eqv_min:16,especi:11,establish:[13,14],etc:[14,22],euclidean:10,evalu:[3,8,22],even:14,ever:22,everi:19,examin:11,exampl:[0,1,2,3,4,6,7,8,10,11,12,13,14,17,22,24],examples_00:15,examples_01:17,except:[0,2,8],execut:[11,15,17],exist:[3,8,11,12],experiment:11,expertis:11,explain:18,expos:[13,19],ext:11,extens:[0,22],extern:2,external_scop:2,extract:[1,3,6,7,13,16,18,24],extract_surfac:6,facilit:11,fals:[11,19],feat:11,featur:18,feedback:11,fetch:16,few:16,field:[2,4,5,6,8,9,10,12,13,15,18,22,24],field_a:10,field_b:10,field_contain:2,field_from_arrai:10,field_max:[13,14,16],field_min:16,field_or_fields_contain:6,field_out:10,field_pb2:3,field_sqr:10,field_sum:10,fieldcontain:10,fields_contain:[3,4,6,12,13,14,16],fields_container_pb2:4,fieldscontain:[5,6,8,10,13],file:[0,3,6,7,8,11,12,13,14,15,16,17,19,22,24],filenam:[7,10],filepath:0,first:[1,11,12,13,14,16,19],fix:11,flag:21,focu:11,focus:11,follow:[11,19],forc:[7,13,14,16,24],fork:11,format:[11,22],fortran:1,foster:11,found:[0,11],fout:10,framework:[7,22],freq:16,frequenc:[12,13,14,16],frequent:22,from:[0,1,2,3,4,6,7,8,10,11,12,13,16,18,21,22,24],full:[11,12,13,14,16,24],gain:11,galleri:[11,12,13,14,16,22],gener:[3,11,12,13,14,16,18,22,23],genuin:19,get:[7,10,12,13,16,19,24],get_entity_data:3,get_entity_data_by_id:3,get_field:4,get_fields_by_time_complex_id:4,get_output:8,gh_token:19,gh_usernam:19,git:[11,21],github:[19,21],give:[5,11],given:[11,13,14],global:[0,3,4,7,8,13],gone:11,grid:6,grpc:[0,2,3,4,6,7,8],guid:11,handl:22,hardwar:22,has:[11,14,22],have:[11,12,13,14,19,20],hdf5:22,help:[6,11,12],here:[11,12,13,14,16,24],highli:13,histori:19,home:24,hope:11,host:[11,19,21],hotfix:11,hourglass_energi:[7,12,13,14,16,22,24],how:[11,12,13,16,18],html:[10,11],html_doc:8,http:[11,20,21],idea:11,ident:14,identifi:11,ids:[2,3,7,14,16,24],ignor:11,ignore_word:11,imag:3,impact:11,implement:11,improv:11,includ:[7,11,12,13,14,16,24],increment:11,incremental_energi:[7,12,13,14,16,22,24],ind:[2,16],index:[1,2,3,4,10,11,13,14,16],indic:[2,16],individu:[7,14,16,24],ineffici:[14,16],info:[12,13,14,16],inform:[11,14,20],initi:0,inplac:13,inpt:8,input:[7,8,10,13,16,24],instal:[11,12,16,20],instanc:[0,3,4,7,8,14,19,24],instead:[14,16],int32:2,interact:13,interfac:22,intern:9,interpert:11,introduc:11,intuit:11,ipynb:[12,13,14,16],isol:[19,21],issu:11,its:[2,11,14,16,22],itself:19,junk:11,jupyt:[12,13,14,16],just:[12,14],kaszynski:11,keep:12,kei:[0,6],keyword:6,kind:11,kinetic_energi:[7,12,13,14,16,22,24],know:11,knowledg:11,kubernet:[19,20],kwarg:[0,6,7,8],label:[11,14,16],label_spac:4,label_space_or_index:4,languag:11,larg:[14,19,22],last:11,latest:[11,21],launch:[11,12,19],layer:[3,6],lead:14,leav:[19,22],legend:16,less:16,lesser:18,let:19,leverag:11,licens:20,like:[3,11,14],limit:[11,22],line:19,link:11,linkcheck:11,linux:[11,24],list:[1,2,3,4,8,11,12,13,14],load:[7,10,16,24],loadstep:[12,13,14,16],local:[0,3,4,7,8,12,20],locat:[1,2,3,7,13,14,16,24],login:19,look:[11,19],low:11,mac:11,machin:[14,21],mai:[4,11,13,16,20],mailto:11,main:[11,14],maint:11,maintain:11,mainten:11,major:11,make:[11,14],mani:11,manipul:22,map:[2,19],map_scop:[2,16],mapdl:[11,22],mapped_data:2,mapping_id_to_index:2,mask:[2,16],master:11,match:[2,10,16,19],materials_field:2,mathemat:22,matplotlib:16,matrix:14,max:[3,13,14,16],max_disp:16,max_disp_z:16,max_field:14,maximum:[3,10,14],mecan:[7,12,13,14,16,22,24],meet:11,member:[2,11],memori:3,mention:11,merg:11,mesh:[1,2,3,6,7,9,12,13,14,16,24],meshed_region:[1,2,3,6,7,12,16,24],meshed_region_pb2:6,meshedregion:[1,5,13],messag:[0,3,4],metadata:[1,2,3,6,7,13,16,23],method:[7,10,11,12,13,16],metric:[7,12,13,14,16,22,24],mid:16,might:[11,14],min:[3,13,14,16],min_disp:16,min_disp_z:16,min_max:[10,13,14,16],min_max_eqv:16,min_max_fc:13,min_max_op:[14,16],minimum:[3,10,11,14],minut:[12,13,14,16],mise:[10,16],misspel:11,mit:11,mm_op:13,mode:11,model:[0,1,2,3,5,6,8,10,13,14,16,22,23],modern:22,modifi:13,modul:[11,12,16,18,21,22],modular:22,more:[3,11,20],much:[11,13],multipl:4,must:[7,10,16,19,24],n_element:2,n_node:1,n_set:[7,16,24],name:[7,8],nativ:20,natur:3,ncomp:3,ndarrai:[2,3],necessari:[11,14,19,21],need:[11,13,16,19,20],nentiti:3,network:21,neutral:22,newer:[11,20,21],next:[11,12,13,16,19],nodal:[3,6,7,10,13,14,16,24],node:[1,2,3,6,12,13,14,16,24],node_by_id:16,node_coord:16,node_id:[1,6,16],none:[0,3,4,6,7,8],norm:[10,13,14,16],norm_fc:13,norm_op:13,normal:19,note:[2,11,12,14,16,19],notebook:[3,6,12,13,14,16],novel:11,now:[11,16,19],num:[3,13,14,16,24],number:[1,2,3,4,7,8,11,12,13,14,16,24],numer:[14,22],numpi:[2,3,10,14,16],numpydoc:11,object:[2,6,8,12,13,14],obtain:11,obviou:11,occur:11,off:6,off_screen:6,often:11,older:11,onc:[11,21],one:[4,10,11],ones:10,onli:[4,10,11,12,16],open:[7,11,12,22,24],oper:[3,5,7,12,14,15,16,18,22,24],operators_help:[10,13,14,16],option:[0,3,4,6,7,8,13],order:[2,13,16],organ:12,origin:11,other:[0,11,13,19,20],otherwis:11,our:11,out:[3,12,13,14,16],outdat:11,outlin:11,output:[2,3,6,8,10,12,13,14,16],outsid:[3,11,14],over:[3,10,14,16],overli:11,overrid:19,overview:[5,15,18,23],packag:[11,19],page:11,pair:19,paradigm:11,paramet:[0,1,2,3,4,6,7,8,10],particular:22,pass:11,password:19,past:11,path:[0,13,24],pep8:11,pep:11,perform:11,period:11,permiss:[11,19],person:19,pertain:11,physic:[7,12,13,14,16,22,24],piec:14,pin:[8,13],pin_out:8,pip:[11,21],pipelin:11,pkg:19,place:[11,12,19],platform:[11,20],pleas:11,plot:[3,6,7,9,16,18],plotter:[5,6],plt:16,plugin:22,point:[6,11,24],point_arrai:6,polydata:6,port:19,portabl:19,possibl:11,post:[11,12,22],potenti:[14,21],power:22,prefer:14,primari:[11,13],primarili:3,print:[1,2,3,6,7,10,12,13,14,16,22,24],probabl:11,process:[10,11,12,22],product:[10,11,22],prohibit:11,project:11,promptli:11,properli:11,properti:[1,2,3,6,7,12,13,14],provid:[11,13,16,22,23,24],push:11,pwd:19,pyansi:[11,19,21],pymapdl:11,pypi:[11,21],pyplot:16,pytest:11,python:[10,11,12,13,14,16,21,22],pyvista:6,pyvista_ndarrai:6,quantiti:22,queri:16,quit:12,random:10,rang:[16,22],rapid:[11,22],rapidli:11,rather:[11,16,19],raw:13,reach:11,read:[7,19,24],reader:11,readi:11,realiz:14,reason:11,recal:14,recurs:0,refer:13,referenc:12,reflect:11,regard:[7,24],regardless:19,region:[1,2,3,6,7,9,12,13,14,16,24],rel:[16,24],relat:24,releas:21,relicens:11,remain:11,remap:[2,16],remot:[0,3,4,7,8,11,12,14],render:6,repeat:11,repo:11,repositori:[19,21],repres:[0,3,4,6,8,22],reproduc:11,request:[4,7,14,16,24],requir:[11,12],requirements_doc:11,requirements_test:11,resiz:3,respect:19,respons:11,restructur:11,restructuredtext:11,result:[0,1,2,3,4,6,7,11,13,14,17,18,22,23],result_info:[7,12,24],result_path:0,retain:14,revert:11,review:11,rinfo:[7,24],roat:13,routin:11,rst:[0,7,8,22,24],rtype:3,run:[8,11,12,13,14,16,19],sacrif:11,same:13,sampl:11,save:[10,19],scalar:2,scale:19,scope:[2,3,4,7,8,13,14,24],scopingid:3,scopingscontain:13,screen:6,screenshot:[6,11],script:[12,13,14,16,19],second:[12,13,14,16],section:[5,11],see:[6,11,16,19,20,22,24],seek:11,seem:14,select:[4,10],select_compon:4,self:[14,22],semant:11,send:19,sent:16,sequenc:11,server:[7,11,12,19,20,24],servic:[11,12,16,19],set:[0,3,4,6,7,11,12,13,14,16,19,24],set_entity_data:3,set_result_file_path:0,setup:11,sever:[5,7,13,16,19,22],shape:[1,3,10,13,14,16,24],share:19,shell:[1,3,6],shell_lay:[3,6],shelllay:[3,6],should:[11,16,19],show:[6,12,16,18],show_ax:6,show_edg:7,side:[11,16],signific:11,silli:11,simpl:[11,22],simple_bar:12,simpli:[14,19],simplifi:10,simul:[14,22],sinc:11,singl:[1,16],singular:19,situat:19,size:[2,3,12],slower:3,softwar:11,solid:1,solut:22,solver:22,some:[11,12,18],someon:11,sometim:11,sourc:[5,7,12,13,14,16,24],special:13,specif:[11,12],specifi:[3,6],speed:16,sphinx:[11,12,13,14,16,18],sqr:10,squar:10,stabil:11,stabl:11,stale:11,standard:11,start:[7,11,12,19,24],start_local_serv:7,state:16,static_rst:[1,2,6,13,14],stdin:19,still:11,store:14,str:[0,3,7,8,13],strain:[7,13,14,16,18,24],stream:13,streamlin:[7,11],streamscontain:13,stress:[3,7,10,13,14,18,24],stress_0:16,string:[3,4,8],structur:[7,24],stub:[0,3],submiss:11,submit:11,subset:14,substep:[12,13,14,16],success:11,suffici:22,suggest:11,suit:11,sum:[7,10],support:[3,11,14,16,20],sure:11,surfac:6,swelling_strain:[7,16,24],symmetr:14,system:[7,12,13,14,16,22,24],tag:11,take:[11,12,14,16,22],target:11,task:11,tdata:16,team:11,technic:11,tell:[11,19],temp:[7,24],temperatur:[7,12,13,14,16,22,24],tensor:[10,14],than:[0,3,11,16],thank:[11,22],thei:[11,19],them:[11,24],therefor:14,thermal_dissipation_energi:[7,12,13,14,16,22,24],thermal_strain:[7,16,24],thermal_strains_eqv:[7,16,24],thi:[0,1,2,3,5,6,7,8,10,11,12,13,14,16,19,21,22,23],thoroughli:11,those:19,thread:11,three:11,through:[8,12,20,22,24],thu:22,time:[3,4,12,13,14,16],time_freq_support:[7,12,16,24],time_scop:16,timeid:[4,16],timestamp:16,titl:11,tmp:0,to_nod:10,togeth:10,token:19,tool:[11,22],toolbox:22,top:3,total:[12,13,14,15,16,17],total_volum:10,traceback:11,track:[11,12],transfer:14,transform:[10,22],trigger:11,trunk:11,tupl:16,two:[10,22],txt:[11,19],type:[1,2,3,4,6,7,10,12,13,14,16,22,24],unabl:21,undefin:19,under:11,understand:11,unintend:11,unit:[3,6,7,11,12,13,14,16,22,24],unit_system:[7,24],unknown_shap:1,unnecessari:14,unordered_map:13,unstabl:11,unstructuredgrid:6,untest:11,until:11,updat:[4,11],upon:[11,22],upstram:0,upstream:0,upstream_data_sourc:0,upstream_id:0,usag:[11,13,14,15,18,19,23,24],use:[4,11,12,14,16,18,19,20,22,24],used:[0,2,3,4,6,7,8,9,12,16,18,24],useful:11,user:[11,13,22,24],usernam:[11,19],uses:[11,19],using:[2,4,7,8,10,11,14,16,19,20,21,24],v2021:19,valid:[7,11],valu:[3,12,13,14,16,19,24],var_inp:10,variabl:[11,19],varieti:[22,24],variou:[13,22,24],vector:[3,10,14],verif:11,verifi:11,version:[11,21],view:24,visit:20,visual:16,vol:2,volum:[2,7,10,12,13,14,16,22,24],von:[10,16],vtk:[6,22],vtkoriginalpointid:6,wai:[2,16],wait:11,want:[13,14],welcom:11,well:[13,22],were:11,what:11,wheel:[11,21],when:[4,6,11,12],whenev:11,where:[11,19],which:[4,8,11,12,14,19,22,24],widget:6,window:[11,19,20],wise:[3,10],wish:[8,12,19,21],within:[11,13,14,19,20,22],without:[11,19,22],word:11,work:[11,13,14],workbench:22,workflow:[0,22],worri:11,would:11,wrap:5,wrapper:10,write:11,www:20,xlabel:16,xxx:11,xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:19,yield:14,ylabel:16,you:[7,8,11,12,14,16,19,20,21,24],your:[11,19],yourself:11,z_coord:16,zen:11,zero:2},titles:["Data Sources Class","Element Class","Elements Class","Field Class","FieldsContainer Class","API Reference","MeshedRegion Class","Model Class","Operator Class","Plotter Class","Wrapped Operators","Contributing","Basic DPF-Core Usage","Operators Overview","Field and Field Containers Overview","Computation times","Transient Analysis Result Example","Computation times","Examples Gallery","Using DPF Through Docker","Getting Started","Installation","PyANSYS DPF-Core","User Guide","The DPF Model"],titleterms:{"class":[0,1,2,3,4,6,7,8,9],"new":11,"transient":[16,18],The:24,Using:19,advanc:18,all:16,analysi:[16,18],api:5,basic:[12,18],branch:11,brief:22,bug:11,build:11,clone:11,code:11,compat:20,comput:[13,15,17],contain:[14,19],continu:11,contribut:11,convent:11,coordin:16,core:[11,12,22],creat:11,data:[0,14],deliveri:11,demo:22,develop:[11,21],displac:[12,13,16],docker:19,document:11,dpf:[11,12,18,19,22,24],edit:21,element:[1,2],exampl:[16,18],extract:[12,14],featur:[11,22],field:[3,14,16],fieldscontain:4,from:[14,19],galleri:18,get:20,github:11,guid:23,guidelin:11,imag:19,instal:[19,21],integr:11,kei:22,licens:11,local:11,maximum:[13,16],meshedregion:6,metadata:[12,24],minimum:16,minor:11,miscellan:18,mode:21,model:[7,11,12,24],name:11,normal:13,obtain:16,oper:[8,10,13],organ:11,overview:[13,14],patch:11,plotter:9,post:16,practic:11,process:16,pull:11,pyansi:22,python:19,question:11,refer:5,releas:11,report:11,repositori:11,request:11,result:[12,16,24],scope:16,sourc:[0,11],spell:11,start:20,step:11,stress:16,style:11,test:11,through:[11,19],time:[15,17],usag:12,user:23,wrap:[10,13]}})