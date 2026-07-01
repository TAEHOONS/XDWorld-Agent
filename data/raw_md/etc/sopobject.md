---
description: 지도 내에 Object를 생성 기능을 관리하는 API 입니다.
---

# SOPObject(추후 삭제 예정 API)

> Module.getAddObject() API를 생성합니다.
>
> 대체 API가 존재합니다.
>
> 추후 삭제 예정입니다

### Add3DPoint(name, key, lon, lat, alt, data, width, height, text)

> 지도에서 POI를 생성합니다.
>
> data 변수는 Uint8Array 기반의 바이너리 배열 데이터 입니다..

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description                |
| :----- | :----- | :------------------------- |
| name   | string | 객체를 생성할 레이어 명칭. |
| key    | string | POI 생성 객체 명칭.        |
| lon    | number | POI 생성 경도 위치.        |
| lat    | number | POI 생성 위도 위치.        |
| alt    | number | POI 생성 고도 위치.        |
| data   | object | 이미지 바이너리 데이터.    |
| width  | number | 이미지의 너비.             |
| height | number | 이미지의 높이.             |
| text   | string | POI에 표시할 글자.         |

-   Sample
    -   function getJudong 참조.
    -   [Sandbox_Building Width Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_building_width)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}
