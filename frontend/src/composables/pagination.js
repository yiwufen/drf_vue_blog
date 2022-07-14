// frontend/src/composables/pagination.js

// 导出三个方法闭包的接口函数
export default function pagination(info, route) {

    const is_page_exists = (direction) => {
      return isPageExists(info, direction)
    };
    const get_page_param = (direction) => {
      return getPageParam(info, route, direction)
    };
    const get_path = (direction) => {
      return getPath(info, direction)
    };
  
    return {
      is_page_exists,
      get_page_param,
      get_path,
    }
  }
  
  // 判断 下一页/上一页 是否存在
  function isPageExists(info, direction) {
    if (direction === 'next') {
      return info.value.next !== null
    }
    return info.value.previous !== null
  }
  
  // 获取页码
  function getPageParam(info, route, direction) {
    try {
      let url_string;
      switch (direction) {
        case 'next':
          url_string = info.value.next;
          break;
        case 'previous':
          url_string = info.value.previous;
          break;
        default:
          return route.query.page
      }
      const url = new URL(url_string);
      return url.searchParams.get('page')
    }
    catch (err) {
      return
    }
  }
  
  // 获取下一页路径
  function getPath(info, direction) {
    let url = '';
    try {
      switch (direction) {
        case 'next':
          if (info.value.next !== undefined) {
            url += (new URL(info.value.next)).search
          }
          break;
        case 'previous':
          if (info.value.previous !== undefined) {
            url += (new URL(info.value.previous)).search
          }
          break;
      }
    }
    catch {
      return url
    }
    return url
  }