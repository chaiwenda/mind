<template>
  <div class="home" style="position: fixed;">
    <div id="part1">
			<div id="search">
			<el-autocomplete
         :value="nodename"
					v-model="searchStr"
					:fetch-suggestions="querySearch"
					placeholder="请输入要搜索的内容"
					:trigger-on-focus="true"
					@select="goToTree"
					id="searchInput"
          
			></el-autocomplete>
			<el-button type="primary" icon="el-icon-search" @click="search">搜索</el-button>
			</div>
			<el-collapse-transition>
			<div id="searchBottom" v-show="showResult">
				<div id="list">
				<el-card shadow="hover" v-for="(item, index) in treeData" v-if="isCurrentList(index)">
					<span @click="goToTreeByClick(index)">{{item["value"]}}</span>
				</el-card>
				</div>
				<el-pagination
						background
						layout="prev, pager, next"
						:page-size="pageSize"
						:total="listSize"
						@current-change="changePage"
				>
				</el-pagination>
			</div>
			</el-collapse-transition>
		</div>
		<div id="part2">思维导图2.1</div>
  </div>
</template>

<script>

    export default {
        name: 'search',
        props:["nodename"],
        data() {
            return {
                loading: false,
                searchStr: "",
								showResult: false,
                listSize: 20,
                treeData: {},
                currentPage: 1,
                pageSize: 5
            }
        },
        methods: {
            search: function() {
                if (this.searchStr) {
                    this.showResult = !this.show;
										this.$emit("update2");
										console.log("1");
                    console.log(this.searchStr);
                    console.log(this.nodename);
                    // this.searchStr="";
                    // this.nodename="";
                }
            },
            querySearch: function (queryString, callback) {
								console.log("2");
                const context = this;
                fetch(`http://localhost:8001/test_api/2/${context.searchStr}/`, {
                    headers:{
                        'content-type':'application/json'
                    }
                }).then(function(response){
                        response.json().then(function(response) {
                            let result = context.formatTreeData(response);
                            context.treeData = result;
                            context.listSize = result.length;
                            callback(result);
                        });
                    }
                );
            },
            formatTreeData(myData) {
								console.log("3");
                let result = [];
                Object.keys(myData).forEach(function (key) {
                    let tempItem = {};
                    let treeBody = myData[key]["Graph"]["tree"];
                    tempItem["tree"] = treeBody;
                    if (treeBody["time"]) {
                        tempItem["value"] = `${treeBody["name"]} (${treeBody["time"]})`;
                    } else {
                        tempItem["value"] = treeBody["name"];
                    }
                    result.push(tempItem);
                });
                return result;
            },
            isCurrentList: function(index) {
                return (index >= (this.currentPage - 1) * this.pageSize) && (index <= (this.currentPage * this.pageSize) - 1);
            },
            changePage: function(page) {
                this.currentPage = page;
            },
            goToTree: function(item) {
                this.$emit('changeTree', item.tree);
            },
            goToTreeByClick: function (index) {
								console.log("7");
								this.showResult = false;
								this.$emit('update');
                this.$emit('changeTree', this.treeData[index]["tree"]);
            }
        }
    }
</script>

<style lang="scss">
  .home {
		position:fixed;
		// background-color: #f8f8f8;
		width: 100%;
		// height: 10%;
		// height: 10%;
		line-height: 45px;
		border-bottom: 1px solid #e1e1e1;
		text-align: center;
		float: left;
    background-color: #ffffff;
    border-radius: 5px;
		/*// border-radius: 1px;*/
    box-shadow: 0px 0px 25px #dcdcdc;
    margin-bottom: 0px;
    /*// padding: 50px;*/
		padding: 10px;
    overflow: auto;
		#part1{
			align-content: left;
			width: 70%;
			float: left;
			#search {
				margin-left: 50%;
				transform: translateX(-50%);
				width: 640px;
				display: flex;
				justify-content: space-around;
				#searchInput {
					width: 500px;
				}
			}
			#searchBottom {
				width: 618px;
				padding: 0 50px;
				margin: 40px auto 20px auto;
				border: 1px solid transparent;
				#list {
					margin-left: -12px;
					height: 340px;
					.el-card {
						width: 632px;
						height: 50px;
						text-align: left;
						margin: 10px 0;
						padding-left: 10px;
            .el-card__body{
              padding:0px;
							span {
									cursor: pointer;
							}
            }
					}
				}
				.el-pagination {
					display: flex;
					justify-content: center;
				}
			}
		}
		#part2 {
    width: 13%;
    float: right;
    font-size: 40px;
    color: aquamarine;
    margin-right: 8%;

}
  }
  
</style>
