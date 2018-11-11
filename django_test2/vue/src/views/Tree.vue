<template>
    <div id="outterContainer" height = "550px" >
				<!-- <div id = 'title-top'> -->
				<Search @changeTree="changeTree" @update="check_update" @update2="check_updata2" v-bind:nodename="deliverInfo"></Search>
				<!-- </div> -->
        <div id="myContainer" v-show='showResult2'>
            <el-container >
							<el-main width = "80%" >
									<tree
													v-show="!treeData.nodeDisplay"
                          :zoomable="treeData.zoomable"
                          :data="treeData.tree"
                          node-text="name"
                          :layoutType="treeData.layoutType"
                          :marginX="treeData.marginx"
                          :marginY="treeData.marginy"
                          :duration="treeData.duration"
                          :type="treeData.type"
                          :radius="treeData.radius"
                          :nodeText="treeData.nodeText2"
                          @clicked="clickNode"
													class="myTree"
												>
									</tree>
                                    <tree
                                                    v-show="treeData.nodeDisplay"
                          :zoomable="treeData.zoomable"
                          :data="treeData.tree"
                          node-text="name"
                          :layoutType="treeData.layoutType"
                          :marginX="treeData.marginx"
                          :marginY="treeData.marginy"
                          :duration="treeData.duration"
                          :type="treeData.type"
                          :radius="treeData.radius"
                          :nodeText="treeData.nodeText"
                          @clicked="clickNode"

                                                    class="myTree"
                                                >
                                    </tree>
							</el-main>
                <el-aside width="20%">
                    <div id="leftBottom">
                        <div class="myHeader">
                            <strong>图片证据展示</strong>
                        </div>
                        <div class="content">
                            <img :src="imgSrc" v-show="showImg" v-on:click="displayimg"/>
                        </div>
                    </div>
										<div id="nodeInfo">
                        <div class="myHeader">
                            <strong>节点信息</strong>
                        </div>
                        <div class="content">                           
                            <p><strong> 节点名称: </strong>  <label v-on:dblclick="setinfo">{{currentInfo}}</label></p><br><br>
                            <p><strong>点击时间: </strong> <label>{{currentTime}}</label></p>
                        </div>
                    </div>
										<div id="leftTop" style="height: 80%;">
												<div class="myHeader">
														<strong>菜单栏</strong>
												</div>
												<div class="content">
														<div class="block">
																<span>图形类型</span>
																<el-select v-model="treeData.type" placeholder="请选择">
																		<el-option
																						v-for="item in typeOptions"
																						:key="item.value"
																						:label="item.label"
																						:value="item.value">
																		</el-option>
																</el-select>
														</div>
														<div class="block">
																<span>图形布局类型</span>
																<el-select v-model="treeData.layoutType" placeholder="请选择">
																		<el-option
																						v-for="item in layoutTypeOptions"
																						:key="item.value"
																						:label="item.label"
																						:value="item.value">
																		</el-option>
																</el-select>
														</div>
														<div class="block">
																<span>图形宽度(px)</span>
																<el-slider
																				:max="1000"
																				:min="-1000"
																				v-model="treeData.marginx"
																				>
																</el-slider>
														</div>
														<div class="block">
																<span>图像高度(px)</span>
																<el-slider
																				:max="200"
																				v-model="treeData.marginy"
																				>
																</el-slider>
														</div>
														<div class="block">
																<span>节点大小(px)</span>
																<el-slider
																				:max="10"
																				:min="2"
																				v-model="treeData.radius"
																				>
																</el-slider>
														</div>
														<div class="block">
																<span>刷新时间(ms)</span>
																<el-slider
																				:max="3000"
																				v-model="treeData.duration"
																				>
																</el-slider>
														</div>
														<div class="block">
                                <label class="zoomable">鼠标交互 <input type="checkbox"  v-model="treeData.zoomable"/>
                                </label>
                                <label class="nodeDisplay">时间展示 <input type="checkbox"  v-model="treeData.nodeDisplay"/>
                                </label>
                                <label><button v-on:click="reset()">重置</button></label>
                                <label><button v-on:click="neo4j1()">连接数据库</button></label>
                            </div>
												</div>
										</div>
                </el-aside>
             
            </el-container>
        </div>
    </div>
</template>

<script>
    import {tree} from 'vued3tree'
    import Search from '../components/Search'

    export default {
        name: 'app',
        components: {
            tree,
            Search
        },
        data() {
            return {
                flag: true,
                typeOptions: [{
                    value: 'tree',
                    label: 'tree'
                }, {
                    value: 'cluster',
                    label: 'cluster'
                }],
                layoutTypeOptions: [{
                    value: 'circular',
                    label: 'circular'
                }, {
                    value: 'euclidean',
                    label: 'euclidean'
                }],
                treeData: {
                    tree: {},
                    marginx: 400,
                    marginy: 100,
                    type: 'tree',
                    layoutType: 'euclidean',
                    radius: 5,
                    duration: 750,
                    zoomable:true,
                    nodeText:'time',
                    nodeDisplay:false,
                    nodeText2:'nodeJname'
                },
                imgSrc: '',
                currentImg: '',
                showImg: false,
								showResult2:true,
								currentInfo:"",
                currentTime:"",
                deliverInfo:"",
            }
        },
        methods: {
						displayimg:function(){
                //this.website=this.website+this.imgSrc+"/";
                //alert(this.website);
                window.open(this.imgSrc,"name", "height=800, width=1500, top=100, left=200, toolbar=no, menubar=no, scrollbars=no, resizable=yes,location=no, status=yes");
               // this.website="http://127.0.0.1:8080/";
            },
						check_update: function(){
								console.log("显示图");
								this.showResult2 = true;
						},
						check_updata2: function(){
								console.log("隐藏图");
								this.showResult2 = false;
						},
            clickNode: function (node) {
                let current = `${node["data"]["name"]} (${node["data"]["time"]})`
                if (this.showImg && this.currentImg === current) {
                    this.showImg = false;
                    this.currentInfo="";
                    this.currentTime="";
                } else {
                    this.currentImg = current;
                    //this.imgSrc = "http://127.0.0.1:8080/"+node["data"]["proof"]+"/";
                    this.imgSrc = node["data"]["proof"];
                    this.showImg = true;
                    this.currentInfo= node["data"]["name"];
                    this.currentTime= node["data"]["time"];
                }
            },
            changeTree: function (newTree) {
                this.treeData.tree = newTree;
                this.showImg = false;
            },
            reset: function(){
                    window.location.reload();
            },
            setinfo: function(){
                    this.deliverInfo=this.currentInfo;
                    console.log(this.deliverInfo);
            },
            neo4j1:function(){
                const neo4j = require('neo4j-driver').v1;

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password));
const session = driver.session();

const personName = 'Alice';
const resultPromise = session.run(
  'CREATE (a:Person {name: $name}) RETURN a',
  {name: personName}
);

resultPromise.then(result => {
  session.close();

  const singleRecord = result.records[0];
  const node = singleRecord.get(0);

  console.log(node.properties.name);

  // on application exit:
  driver.close();
});
            }

        },
        mounted() {
             const context = this;
             if(this.flag == true){
                 console.log(this.flag == true);
                fetch(`http://localhost:8001/test_api/2/开始/`, {
                headers:{
                    'content-type':'application/json'
                }
            }).then(function(response){
                    response.json().then(function(response) {
                        context.treeData.tree = response[0]["Graph"]["tree"];
                    });
                }
            );
                this.flag = false;
                console.log(this.flag);
            }
        }
    }
</script>

<style lang="scss">
    @import '../style/reset.css';
    body {
        background-color: #f4f5f5;
        background-image: url("../assets/1.jpg");
        background-repeat: no-repeat;
        background-size: 3000px auto;
    }
    body::-webkit-scrollbar {
        display:none;
        /*width:1800px;*/
    }
    strong{
        font-weight: bold;
    }
		.outterContainer {
			height: 10px;
		}
    .el-container {
         /*width: 1300px;*/
				width: 98%;
        /*margin-top: 10px;*/
        height:1200px;
        margin: 0px;
        margin-right: 0px;
    }

    .el-main {
        background-color: #f0f8f8;
        /*border: 1px solid #e1e1e1;*/
        border-radius: 5px;
        /*margin-right: 1%;*/
        height:70%;
        width: 80%;
    }
		
    .el-aside {
				background-color:#F8F8F8;
                height:70%;
                width:20%;
                margin:0px;
			#nodeInfo{
             background-color: #ffffff;
            border: 1px solid #e1e1e1;
            border-radius: 5px;
            margin-bottom: 30px;
            margin-top:30px;
            margin-left:10px;
            height: 20%;
            .myHeader {
                background-color: #888888;
                height: 45px;
                line-height: 45px;
                border-bottom: 1px solid #e1e1e1;
                text-align: center;
                font-size: 23px;
            }
			}
            #leftTop, #leftBottom {
            background-color: #ffffff;
            border: 1px solid #e1e1e1;
            border-radius: 5px;
            height:25%;
            margin-top: 20px;
						margin-left: 10px;
					    /*margin-bottom: 30px;*/
            .myHeader {
                background-color: #888888;
                height: 45px;
                line-height: 45px;
                border-bottom: 1px solid #e1e1e1;
                text-align: center;
                font-size: 23px;
            }
						#title-top{
							background-color: #f8f8f8;
							float: left;
							height: 8%;
							width: 100%;
							#title1 {
									width: 30%;
									float: right;
									height: 100%;
									display: inline-block;
									font-family: "等线";
									font-size: 40px;
									font-weight: bolder;
									color: #70e1bd;
							}
						}
            .content {
								height: 90%;
								font-size: 10px;
                /*padding: 10px 10px 10px 10px;*/
                img {
                    width: 100%;
                    height:100%;
                }
                .block {
                    margin: 10px 0;
                    display: flex;
                    span {
                        padding: 10px 0;
                        text-align: right;
                        width: 135px;
                        margin-right: 10px;
                        font-weight: 600;
                    }
                    .el-slider {
                        width: 100%;
                    }
                }
                .el-select {
                    width: 100%;
                }
            }
        }
				
    }
    #myHeader {
        text-align: center;
        z-index: 1000;
        position: fixed;
        width: 100%;
        height: 60px;
        background-color: #ffffff;
        border-bottom: 1px solid #e1e1e1;
        line-height: 60px;
    }
    #myContainer {
			padding-top: 5%;
			padding-left: 1%;
            width:100%;
}
    .myTree {
        height: 1500px;
        width: 99%;
    }
		tree{
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .treeclass .linktree{
        stroke:#000;
        stroke-width:2px;

    }
    .treeclass .nodetree text{
            font: 16px sans-serif;
        }
</style>
