import API from './api';
import qs from 'querystring';

export function getAllTracks(page = 1, limit = 10) {
    const queryParams = {page, limit };
    const queryString = qs.stringify(queryParams);
    
    return API.get(`/tracks/list?${queryString}`).then(response => response.data);
}