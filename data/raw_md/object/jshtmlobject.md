---
description: 지도 내 경로 기능을 관리하기 위한 API 입니다.
---

# JSHTMLObject

> Module.createHTMLObject() API를 생성합니다.

```javascript
let trace = Module.createHTMLObject("ID");
```

## Properties

| Name            | Type                                | Description                                               |
| --------------- | ----------------------------------- | --------------------------------------------------------- |
| element 		  | HTML element                        | JSHTMLObject element. 								|
| verticalAlign   | string                              | JSHTMLObject 가시화 수평 정렬 설정 (left, center, right). |
| horizontalAlign | string                              | JSHTMLObject 가시화 수직 정렬 설정 (top, middle, bottom). |
| position        | [JSVector3D](../core/jsvector3d.md) | 중심 좌표 설정 (경도, 위도, 고도).                        |

## Function

### createbyJson(option) -> object

> HTML Element 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                                                     | Description |
| :----- | :----------------------------------------------------------------------- | :---------- |
| option | [JSHTMLObject.CreateOptions](jshtmlobject.md#jshtmlobject.createoptions) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( 문자열 : 실패 에러 코드 ).
-   Sample
    -   function createDivObject 참조.
    -   [Sandbox_HTML_Media](https://sandbox.egiscloud.com/code/main.do?id=object_html)

{% endtab %}

{% tab title="Template" %}

```javascript
let element = document.createElement("div");
let parameter = {
    position: new Module.JSVector3D(129.13782351349964, 35.17887462859219, 400.0),
    container: "divcontainer",
    canvas: Module.canvas,
    element: element,
};
let object = Module.createHTMLObject("div_object");
object.createbyJson(parameter);
```

{% endtab %}
{% endtabs %}

### refresh()

> 객체 가시화를 갱신합니다.
>
> 객체 옵션 변경에 따른 가시화 변경 사항을 즉시 적용합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}

{% tab title="Template" %}

```javascript
// Omission of object creation and connection process.
object.refresh();
```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSHTMLObject.CreateOptions

> HTML 객체 생성 옵션.

| Name            | Type                                | Attributes | Default | Description                           |
| --------------- | ----------------------------------- | ---------- | ------- | ------------------------------------- |
| position        | [JSVector3D](../core/jsvector3d.md) |            |         | 중심 좌표 (경도, 위도, 고도).         |
| container       | string                              |            |         | web element를 보관할 컨테이너 명칭.   |
| canvas          | web element                         |            |         | 화면 크기 설정을 위한 캔버스 element. |
| element         | web element                         |            |         | 가시화 할 web element.                |
| verticalAlign   | string                              | optional   | top     | 가시화 옵션(수직 정렬).               |
| horizontalAlign | string                              | optional   | left    | 가시화 옵션(수평 정렬).               |
| moveChange      | function                            | optional   |         | 가시화 변경 시점 콜백 함수.           |
