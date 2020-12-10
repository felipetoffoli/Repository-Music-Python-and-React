import API from './api';
import qs from 'querystring';

export function getAllTracks(page = 1, search = '', limit = 5) {
    const queryParams = { page, search, limit };
    const queryString = qs.stringify(queryParams);

    return API.get(`/tracks/list?${queryString}`).then(response => response.data);
}


export function uploadTrack(file, name) {
    var formData = new FormData();

    formData.append("file", file);
    formData.append("name", name);

    return API({
        method: 'POST',
        url: '/tracks',
        data: formData,
        headers: {'Content-Type': 'multipart/form-data' }
    })
}