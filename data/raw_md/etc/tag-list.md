# Tag List

### coordinates Type

| Name       | Type                                                         | Description                         |
| ---------- | ------------------------------------------------------------ | ----------------------------------- |
| coordinate | object                                                       | 경위도 좌표 목록.                   |
| style      | [coordinates Style Type](tag-list.md#coordinates-style-type) | 경위도 좌표 목록을 구성하는 스타일. |

### coordinates Style Type

| Name                                | Type   | Description                    |
| ----------------------------------- | ------ | ------------------------------ |
| XY                                  | string | \[\[x, y], \[x, y], ...]       |
| XYZ                                 | string | \[\[x, y, z], \[x, y, z], ...] |
| XYZARRAY                            | string | \[x, y, z, x, y, z,...]        |
| [JSVector3D](../core/jsvector3d.md) | string | \[JSVector3D, JSVector3D, ...] |

### Interpolation Type

| Name      | Type                                | Description  |
| --------- | ----------------------------------- | ------------ |
| position  | [JSVector2D](../core/jsvector2d.md) | 경위도 좌표. |
| direction | number                              | 진행 방향.   |
| strength  | number                              | 진행 세기.   |

### Range2D Style Type

| Name | Type   | Description         |
| ---- | ------ | ------------------- |
| min  | number | 좌하단 경위도 좌표. |
| max  | number | 우상단 경위도 좌표. |

### Rect2D Style Type

| Name | Type                                | Description         |
| ---- | ----------------------------------- | ------------------- |
| min  | [JSVector2D](../core/jsvector2d.md) | 좌하단 경위도 좌표. |
| max  | [JSVector2D](../core/jsvector2d.md) | 우상단 경위도 좌표. |

### Size2D Style Type

| Name 	 | Type                                	| Description         	|
| ------ | ------------------------------------ | --------------------- |
| width  | number 								| 넓이. 					|
| height | number 								| 높이. 					|