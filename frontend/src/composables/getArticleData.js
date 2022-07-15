// frontend/src/composables/getArticleData.js

import axios from 'axios';
import {onMounted, watch} from 'vue'

export default function getArticleData(info, route, kwargs) {
  const getData = async () => {
    // 函数起始处对当前 query 参数进行等值判断
    // 若为重复请求则立即中断函数
    const queryPage = route.query.page !== undefined ? parseInt(route.query.page) : 1;
    if (kwargs.value.page === queryPage && kwargs.value.searchText === route.query.search) {
      return
    }

    let url = '/api/article';
    let params = new URLSearchParams();

    params.appendIfExists('page', route.query.page);
    params.appendIfExists('search', route.query.search);

    const paramsString = params.toString();
    if (paramsString.charAt(0) !== '') {
      url += '/?' + paramsString
    }

    const response = await axios.get(url);
    info.value = response.data;
    
    // 函数末尾对当前页的状态赋值
    // 用于下次请求时进行重复性判断
    kwargs.value.page = queryPage;
    kwargs.value.searchText = route.query.search;
  };

  onMounted(getData);
  watch(route, getData);
}